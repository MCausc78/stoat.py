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

from datetime import datetime
import typing

from attrs import define, field


@define(slots=True)
class InstanceCaptchaFeature:
    """Configuration for hCaptcha on Revolt instance."""

    enabled: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the CAPTCHA is enabled on current instance."""

    key: str = field(repr=True, kw_only=True)
    """:class:`str`: The client key used for solving CAPTCHA."""


@define(slots=True)
class InstanceGenericFeature:
    """Represents how one of Revolt instance services is configured."""

    enabled: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the service is enabled on current instance."""

    url: str = field(repr=True, kw_only=True)
    """:class:`str`: The URL pointing to the service."""


@define(slots=True)
class InstanceLivekitVoiceNode:
    """Represents a Livekit node."""

    name: str = field(repr=True, kw_only=True)
    """:class:`str`: The node's name."""

    latitude: float = field(repr=True, kw_only=True)
    """:class:`float`: The latitude."""

    longitude: float = field(repr=True, kw_only=True)
    """:class:`float`: The longitude."""

    public_url: str = field(repr=True, kw_only=True)
    """:class:`str`: The node's public WebSocket URL."""


@define(slots=True)
class InstanceVosoVoiceFeature:
    """Represents how Voso voice server is configured on Revolt instance."""

    enabled: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the voice server is enabled on current instance."""

    url: str = field(repr=True, kw_only=True)
    """:class:`str`: The URL pointing to the voice HTTP server."""

    websocket_url: str = field(repr=True, kw_only=True)
    """:class:`str`: The URL pointing to the voice WebSocket server."""

    def is_voso(self) -> typing.Literal[True]:
        return True

    def is_livekit(self) -> typing.Literal[False]:
        return False


@define(slots=True)
class InstanceLivekitVoiceFeature:
    """Represents how Livekit voice server is configured on Revolt instance."""

    enabled: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether the voice server is enabled on current instance."""

    nodes: list[InstanceLivekitVoiceNode] = field(repr=True, kw_only=True)
    """List[:class:`.InstanceLivekitVoiceNode`]: The Livekit nodes on this instance."""

    def is_voso(self) -> typing.Literal[False]:
        return False

    def is_livekit(self) -> typing.Literal[True]:
        return True


InstanceVoiceFeature = typing.Union[
    InstanceVosoVoiceFeature,
    InstanceLivekitVoiceFeature,
]


@define(slots=True)
class InstanceFeaturesConfig:
    """Represents how features are configured on this Revolt instance."""

    captcha: InstanceCaptchaFeature = field(repr=True, kw_only=True)
    """:class:`.InstanceCaptchaFeature`: The CAPTCHA configuration."""

    email_verification: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether is E-Mail verification required."""

    invite_only: bool = field(repr=True, kw_only=True)
    """:class:`bool`: Whether this server is invite only."""

    autumn: InstanceGenericFeature = field(repr=True, kw_only=True)
    """:class:`.InstanceGenericFeature`: The configuration for Autumn (file server service)."""

    january: InstanceGenericFeature = field(repr=True, kw_only=True)
    """:class:`.InstanceGenericFeature`: The configuration for January (embed server service)."""

    voice: InstanceVoiceFeature = field(repr=True, kw_only=True)
    """:class:`.InstanceVoiceFeature`: The configuration for Vortex or Livekit (voice server service)."""


# Sample build object (own instance):
# "build": {
#  "commit_sha": "b27895725b2eae5bab05b5d9c6ed6452a4a6fbcc",
#  "commit_timestamp": "2024-07-06T17:18:24Z",
#  "semver": "20231026-01-131-gb278957",
#  "origin_url": "https://github.com/MCausc78/revoltchat-backend",
#  "timestamp": "2024-08-07T19:28:05.5951601Z"
# }


@define(slots=True)
class InstanceBuild:
    """Represents information about instance build.

    .. warning::
        Some fields might be None, empty string or have ``'<failed to generate>'`` value if they are unavailable.
        Never assume that they will be available.
    """

    commit_as_sha: str = field(repr=True, kw_only=True)
    """:class:`str`: The commit hash. For example: ``'a52d610e6c152e7acc23cd017a7c67af46eace4c'``."""

    committed_at: typing.Optional[datetime] = field(repr=True, kw_only=True)
    """Optional[:class:`~datetime.datetime`]: When last commit was at."""

    semver: str = field(repr=True, kw_only=True)
    """:class:`str`: The build tag. Example: ``'20240710-1-157-ga52d610'``."""

    origin_url: str = field(repr=True, kw_only=True)
    """:class:`str`: The origin URL. Example: ``'https://github.com/revoltchat/backend'``."""

    built_at: typing.Optional[datetime] = field(repr=True, kw_only=True)
    """Optional[:class:`~datetime.datetime`]: When the instance executables were built at. This is different from :attr:`.committed_at`."""


@define(slots=True)
class Instance:
    """Represents a Revolt instance."""

    version: str = field(repr=True, kw_only=True)
    """:class:`str`: The API version."""

    features: InstanceFeaturesConfig = field(repr=True, kw_only=True)
    """:class:`.InstanceFeaturesConfig`: The configuration of features enabled on this Revolt node."""

    websocket_url: str = field(repr=True, kw_only=True)
    """:class:`str`: The WebSocket URL."""

    app_url: str = field(repr=True, kw_only=True)
    """:class:`str`: The web application URL."""

    vapid_public_key: str = field(repr=True, kw_only=True)
    """:class:`str`: The VAPID public key, used for WebPush."""

    build: InstanceBuild = field(repr=True, kw_only=True)
    """:class:`.InstanceBuild`: The information of build of this instance."""


__all__ = (
    'InstanceCaptchaFeature',
    'InstanceGenericFeature',
    'InstanceLivekitVoiceNode',
    'InstanceVosoVoiceFeature',
    'InstanceLivekitVoiceFeature',
    'InstanceVoiceFeature',
    'InstanceFeaturesConfig',
    'InstanceBuild',
    'Instance',
)
