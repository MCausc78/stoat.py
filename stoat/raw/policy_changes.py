from __future__ import annotations

import typing


class PolicyChange(typing.TypedDict):
    created_time: str
    effective_time: str
    description: str
    url: str
