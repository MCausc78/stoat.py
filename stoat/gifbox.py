"""
The MIT License (MIT)

Copyright (c) 2024-present MCausc78

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

from inspect import isawaitable
import logging
import typing

from attrs import define, field
from multidict import CIMultiDict

from . import __version__, utils
from .adapter import HTTPResponse, HTTPAdapter, AIOHTTPAdapter
from .errors import HTTPException

if typing.TYPE_CHECKING:
    from . import raw
    from .state import State


_L = logging.getLogger(__name__)
DEFAULT_GIFBOX_USER_AGENT = f'stoat.py (https://github.com/MCausc78/stoat.py, {__version__})'


@define(slots=True, eq=True)
class GIFCategory:
    """Represents a GIF category.

    .. versionadded:: 1.3
    """

    title: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The category's name."""

    preview_url: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The URL for the GIF for category."""


@define(slots=True, eq=True)
class GIF:
    """Represents a GIF retrieved from Tenor proxy.

    .. versionadded:: 1.3
    """

    id: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The ID of the GIF."""

    url: str = field(repr=True, kw_only=True)
    """:class:`str`: The URL for the GIF."""

    media_formats: dict[str, OtherGIF] = field(repr=True, kw_only=True)
    """Dict[:class:`str`, :class:`OtherGIF`]: A mapping of `media formats <https://developers.google.com/tenor/guides/response-objects-and-errors#format-types>`_ to equivalent of this GIF in other format."""


@define(slots=True, eq=True)
class OtherGIF:
    """Represents a GIF in other format.

    .. versionadded:: 1.3
    """

    url: str = field(repr=True, kw_only=True, eq=True)
    """:class:`str`: The URL for the GIF."""

    dimensions: tuple[int, int] = field(repr=True, kw_only=True, eq=True)
    """Tuple[:class:`int`, :class:`int`]: A tuple representing width and height in pixels."""


class GIFBoxClient:
    """Represents a HTTP client sending HTTP requests to the GIFBox API.

    .. versionadded:: 1.3

    Attributes
    ----------
    state: :class:`State`
        The state.
    user_agent: :class:`str`
        The HTTP user agent used when making requests.
    """

    __slots__ = (
        '_adapter',
        '_base',
        'state',
        'user_agent',
    )

    def __init__(
        self,
        *,
        base: typing.Optional[str] = None,
        adapter: typing.Optional[
            typing.Union[utils.MaybeAwaitableFunc[[GIFBoxClient], HTTPAdapter], HTTPAdapter]
        ] = None,
        state: State,
        user_agent: typing.Optional[str] = None,
    ) -> None:
        if base is None:
            base = 'https://api.gifbox.me'

        self._adapter: typing.Optional[
            typing.Union[utils.MaybeAwaitableFunc[[GIFBoxClient], HTTPAdapter], HTTPAdapter]
        ] = adapter
        self._base = base.rstrip('/')
        self.state: State = state
        self.user_agent: str = user_agent or DEFAULT_GIFBOX_USER_AGENT

    async def get_adapter(self) -> HTTPAdapter:
        if self._adapter is None:
            adapter = AIOHTTPAdapter()
            self._adapter = adapter
            return adapter

        if callable(self._adapter):
            ret = self._adapter(self)
            if isawaitable(ret):
                ret = await ret
            await ret.startup()
            self._adapter = ret
            return ret

        return self._adapter

    def maybe_get_adapter(self) -> typing.Optional[HTTPAdapter]:
        if self._adapter is None or not isinstance(self._adapter, HTTPAdapter):
            return None
        return self._adapter

    @property
    def adapter(self) -> HTTPAdapter:
        if self._adapter is None or (callable(self._adapter) and not isinstance(self._adapter, HTTPAdapter)):
            raise TypeError('No adapter is available')
        return self._adapter

    @property
    def base(self) -> str:
        """:class:`str`: The base URL."""
        return self._base

    @property
    def bot(self) -> bool:
        """:class:`bool`: Whether the token belongs to bot account."""
        return self.state.http.bot

    @property
    def oauth2(self) -> bool:
        """:class:`bool`: Whether the token is an OAuth2 access token."""
        return self.state.http.oauth2

    @property
    def token(self) -> str:
        """:class:`str`: The token in use. May be empty if not started."""
        return self.state.http.token

    async def raw_request(self, method: str, path: str, /, **kwargs) -> HTTPResponse:
        headers: CIMultiDict[str]

        try:
            tmp = kwargs.pop('headers')
        except KeyError:
            headers = CIMultiDict()
        else:
            headers = CIMultiDict(tmp)

        if kwargs.pop('authenticated', True):
            if self.bot:
                th = 'X-Bot-Token'
            elif self.oauth2:
                th = 'X-OAuth2-Token'
            else:
                th = 'X-Session-Token'
            headers[th] = self.token

        if not kwargs.pop('manual_accept', False):
            headers['Accept'] = 'application/json'

        headers['User-Agent'] = self.user_agent

        url = self._base + path

        _L.debug('Sending request to %s', path)

        adapter = await self.get_adapter()

        response = await adapter.request(
            method,
            url,
            headers=headers,
            **kwargs,
        )
        if response.status >= 400:
            data = await utils._json_or_text(response)
            if isinstance(data, dict) and isinstance(data.get('error'), dict):
                error = data['error']
                code = error.get('code')
                reason = error.get('reason')
                description = error.get('description')
                data['type'] = 'Rocket error'
                data['err'] = f'{code} {reason}: {description}'

            from .http import _STATUS_TO_ERRORS

            raise _STATUS_TO_ERRORS.get(response.status, HTTPException)(response, data)
        return response

    async def request(self, method: str, path: str, /, **kwargs) -> typing.Any:
        await self.raw_request(method, path)

    async def get_trending_categories(self, *, locale: str = 'en_US') -> list[GIFCategory]:
        """|coro|

        Retrieve trending GIF categories.

        Parameters
        ----------
        locale: :class:`str`
            The locale the categories should be returned in. Defaults to ``en_US``.

        Returns
        -------
        List[:class:`GIFCategory`]
            The trending GIF categories.
        """
        resp: list[raw.gb.CategoryResponse] = await self.request(
            'GET', '/categories', params={'locale': locale}
        )  # CategoriesResponse[]
        return list(map(self.state.parser.parse_gif_category, resp))

    async def get_service_version(self) -> str:
        """|coro|

        Retrieves GIF service's version.

        Returns
        -------
        :class:`str`
            The version of the GIF service.
        """
        resp: raw.gb.RootResponse = await self.request('GET', '/')
        return resp['version']

    async def search(
        self,
        query: str,
        *,
        locale: str = 'en_US',
        limit: typing.Optional[int] = None,
        is_category: typing.Optional[bool] = None,
        position: typing.Optional[str] = None,
    ) -> tuple[list[GIF], typing.Optional[str]]:
        """|coro|

        Searches for GIFs.

        Parameters
        ----------
        query: :class:`str`
            The query to search GIFs by.
        locale: :class:`str`
            The locale the GIFs should be returned in. Defaults to ``en_US``.
        limit: Optional[:class:`int`]
            The maximum number of GIFs to get. Must be between 1 and 50. Defaults to 20.
        is_category: Optional[:class:`bool`]
            Unknown. Used for analytics.
        position: Optional[:class:`str`]
            The position to get GIFs from.

        Returns
        -------
        Tuple[List[:class:`GIF`], Optional[:class:`str`]]
            The GIF results returned from Tenor proxy API and the position to get next GIFs by.
        """
        params: raw.gb.SearchQueryParams = {
            'query': query,
            'locale': locale,
        }
        if limit is not None:
            params['limit'] = limit
        if is_category is not None:
            params['is_category'] = utils._bool(is_category)
        if position is not None:
            params['position'] = position

        resp: raw.gb.PaginatedMediaResponse = await self.request('GET', '/search', params=params)
        return (list(map(self.state.parser.parse_gif, resp['results'])), resp.get('next'))


__all__ = (
    'DEFAULT_GIFBOX_USER_AGENT',
    'GIFCategory',
    'GIF',
    'OtherGIF',
    'GIFBoxClient',
)
