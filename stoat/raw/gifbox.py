from __future__ import annotations

import typing
import typing_extensions

from .basic import Bool


# >> /routes/categories.rs
class CategoriesQueryParams(typing.TypedDict):
    locale: str


# >> /routes/search.rs
class SearchQueryParams(typing.TypedDict):
    query: str
    locale: str
    limit: typing_extensions.NotRequired[int]
    is_category: typing_extensions.NotRequired[Bool]
    position: typing_extensions.NotRequired[str]


# >> /types.rs
class RootResponse(typing.TypedDict):
    message: str
    version: str


class PaginatedMediaResponse(typing.TypedDict):
    results: list[MediaResult]
    next: typing_extensions.NotRequired[str]


class MediaResult(typing.TypedDict):
    id: str
    media_formats: dict[str, MediaObject]
    url: str


class MediaObject(typing.TypedDict):
    url: str
    dimensions: tuple[int, int]


class CategoryResponse(typing.TypedDict):
    title: str
    image: str
