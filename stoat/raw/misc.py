from __future__ import annotations

import typing
import typing_extensions


class CaptchaFeature(typing.TypedDict):
    enabled: bool
    key: str


class Feature(typing.TypedDict):
    enabled: bool
    url: str


class LivekitVoiceNode(typing.TypedDict):
    name: str
    lat: float
    lon: float
    public_url: str


class VosoVoiceFeature(typing.TypedDict):
    enabled: bool
    url: str
    ws: str


class LivekitVoiceFeature(typing.TypedDict):
    enabled: bool
    nodes: list[LivekitVoiceNode]


class StoatFeatures(typing.TypedDict):
    captcha: CaptchaFeature
    email: bool
    invite_only: bool
    autumn: Feature
    january: Feature
    voso: VosoVoiceFeature
    livekit: typing_extensions.NotRequired[LivekitVoiceFeature]


class BuildInformation(typing.TypedDict):
    commit_sha: str
    commit_timestamp: str
    semver: str
    origin_url: str
    timestamp: str


class StoatConfig(typing.TypedDict):
    revolt: str
    features: StoatFeatures
    ws: str
    app: str
    vapid: str
    build: BuildInformation
