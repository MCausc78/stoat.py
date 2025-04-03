"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

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

# Thanks Danny https://github.com/Rapptz/discord.py/blob/7d3eff9d9d115dc29b5716c42eaeedf1a008e9b0/discord/enums.py
from __future__ import annotations

from collections import namedtuple
from datetime import datetime
import types
import typing

from .utils import _UTC

if typing.TYPE_CHECKING:
    from collections.abc import Iterator, Mapping


def _create_value_cls(name: str, comparable: bool, /):
    # All the type ignores here are due to the type checker being unable to recognise
    # Runtime type creation without exploding.
    cls = namedtuple('_EnumValue_' + name, 'name value')
    cls.__repr__ = lambda self: f'<{name}.{self.name}: {self.value!r}>'  # type: ignore
    cls.__str__ = lambda self: f'{name}.{self.name}'  # type: ignore
    if comparable:
        cls.__le__ = lambda self, other: isinstance(other, self.__class__) and self.value <= other.value  # type: ignore
        cls.__ge__ = lambda self, other: isinstance(other, self.__class__) and self.value >= other.value  # type: ignore
        cls.__lt__ = lambda self, other: isinstance(other, self.__class__) and self.value < other.value  # type: ignore
        cls.__gt__ = lambda self, other: isinstance(other, self.__class__) and self.value > other.value  # type: ignore
    return cls


def _is_descriptor(obj: typing.Any, /) -> bool:
    return hasattr(obj, '__get__') or hasattr(obj, '__set__') or hasattr(obj, '__delete__')


class EnumMeta(type):
    if typing.TYPE_CHECKING:
        __name__: typing.ClassVar[str]  # type: ignore
        _enum_member_names_: typing.ClassVar[list[str]]
        _enum_member_map_: typing.ClassVar[dict[str, typing.Any]]
        _enum_value_map_: typing.ClassVar[dict[typing.Any, typing.Any]]

    def __new__(
        cls,
        name: str,
        bases: tuple[type, ...],
        attrs: dict[str, typing.Any],
        /,
        *,
        comparable: bool = False,
    ) -> EnumMeta:
        value_mapping = {}
        member_mapping = {}
        member_names = []

        value_cls = _create_value_cls(name, comparable)
        for key, value in list(attrs.items()):
            is_descriptor = _is_descriptor(value)
            if key[0] == '_' and not is_descriptor:
                continue

            # Special case classmethod to just pass through
            if isinstance(value, classmethod):
                continue

            if is_descriptor:
                setattr(value_cls, key, value)
                del attrs[key]
                continue

            try:
                new_value = value_mapping[value]
            except KeyError:
                new_value = value_cls(name=key, value=value)
                value_mapping[value] = new_value
                member_names.append(key)

            member_mapping[key] = new_value
            attrs[key] = new_value

        attrs['_enum_value_map_'] = value_mapping
        attrs['_enum_member_map_'] = member_mapping
        attrs['_enum_member_names_'] = member_names
        attrs['_enum_value_cls_'] = value_cls
        actual_cls = super().__new__(cls, name, bases, attrs)
        value_cls._actual_enum_cls_ = actual_cls  # type: ignore # Runtime attribute isn't understood
        return actual_cls

    def __iter__(cls) -> Iterator[typing.Any]:
        return (cls._enum_member_map_[name] for name in cls._enum_member_names_)

    def __reversed__(cls) -> Iterator[typing.Any]:
        return (cls._enum_member_map_[name] for name in reversed(cls._enum_member_names_))

    def __len__(cls) -> int:
        return len(cls._enum_member_names_)

    def __repr__(cls) -> str:
        return f'<enum {cls.__name__}>'

    @property
    def __members__(cls) -> Mapping[str, typing.Any]:
        return types.MappingProxyType(cls._enum_member_map_)

    def __call__(cls, value: str, /) -> typing.Any:
        # try:
        return cls._enum_value_map_[value]
        # except (KeyError, TypeError):
        # raise ValueError(f'{value!r} is not a valid {cls.__name__}')

    def __getitem__(cls, key: str, /) -> typing.Any:
        return cls._enum_member_map_[key]

    def __setattr__(cls, name: str, value: typing.Any, /) -> None:
        raise TypeError('Enums are immutable.')

    def __delattr__(cls, attr: str, /) -> None:
        raise TypeError('Enums are immutable.')

    def __instancecheck__(self, instance: typing.Any, /) -> bool:
        # isinstance(x, Y)
        # -> __instancecheck__(Y, x)
        try:
            return instance._actual_enum_cls_ is self
        except AttributeError:
            return False


if typing.TYPE_CHECKING:
    from enum import Enum
else:

    class Enum(metaclass=EnumMeta):
        """An enum class that mimics behavior of :class:`enum.Enum`."""

        @classmethod
        def try_value(cls, value) -> typing.Any:
            try:
                return cls._enum_value_map_[value]
            except (KeyError, TypeError):
                return value


class MFAMethod(Enum):
    password = 'Password'
    recovery = 'Recovery'
    totp = 'Totp'


class AssetMetadataType(Enum):
    file = 'File'
    text = 'Text'
    image = 'Image'
    video = 'Video'
    audio = 'Audio'


class ChannelType(Enum):
    saved_messages = 'SavedMessages'
    private = 'DirectMessage'
    group = 'Group'
    text = 'Text'
    voice = 'Voice'

    unknown = ''


class ServerActivity(Enum):
    high = 'high'
    medium = 'medium'
    low = 'low'
    no = 'no'


class BotUsage(Enum):
    high = 'high'
    medium = 'medium'
    low = 'low'


class LightspeedContentType(Enum):
    channel = 'Channel'


class TwitchContentType(Enum):
    channel = 'Channel'
    video = 'Video'
    clip = 'Clip'


class BandcampContentType(Enum):
    album = 'Album'
    track = 'Track'


class ImageSize(Enum):
    large = 'Large'
    preview = 'Preview'


class Language(Enum):
    english = 'en'
    english_simplified = 'en_US'

    arabic = 'ar'
    assamese = 'as'
    azerbaijani = 'az'
    belarusian = 'be'
    bulgarian = 'bg'
    bengali = 'bn'
    breton = 'br'
    catalonian = 'ca'
    cebuano = 'ceb'
    central_kurdish = 'ckb'
    czech = 'cs'
    danish = 'da'
    german = 'de'
    greek = 'el'
    spanish = 'es'
    spanish_latin_america = 'es_419'
    estonian = 'et'
    finnish = 'fi'
    filipino = 'fil'
    french = 'fr'
    irish = 'ga'
    hindi = 'hi'
    croatian = 'hr'
    hungarian = 'hu'
    armenian = 'hy'
    indonesian = 'id'
    icelandic = 'is'
    italian = 'it'
    japanese = 'ja'
    korean = 'ko'
    luxembourgish = 'lb'
    lithuanian = 'lt'
    macedonian = 'mk'
    malay = 'ms'
    norwegian_bokmal = 'nb_NO'
    dutch = 'nl'
    persian = 'fa'
    polish = 'pl'
    portuguese_brazil = 'pt_BR'
    portuguese_portugal = 'pt_PT'
    romanian = 'ro'
    russian = 'ru'
    slovak = 'sk'
    slovenian = 'sl'
    albanian = 'sq'
    serbian = 'sr'
    sinhalese = 'si'
    swedish = 'sv'
    tamil = 'ta'
    thai = 'th'
    turkish = 'tr'
    ukranian = 'uk'
    urdu = 'ur'
    venetian = 'vec'
    vietnamese = 'vi'
    chinese_simplified = 'zh_Hans'
    chinese_traditional = 'zh_Hant'
    latvian = 'lv'

    tokipona = 'tokipona'
    esperanto = 'esperanto'

    owo = 'owo'
    pirate = 'pr'
    bottom = 'bottom'
    leet = 'leet'
    piglatin = 'piglatin'
    enchantment_table = 'enchantment'


class MessageSort(Enum):
    relevance = 'Relevance'
    latest = 'Latest'
    oldest = 'Oldest'


class ContentReportReason(Enum):
    none = 'NoneSpecified'
    illegal = 'Illegal'
    illegal_goods = 'IllegalGoods'
    illegal_extortion = 'IllegalExtortion'
    illegal_pornography = 'IllegalPornography'
    illegal_hacking = 'IllegalHacking'
    extreme_violence = 'ExtremeViolence'
    promotes_harm = 'PromotesHarm'
    unsolicited_spam = 'UnsolicitedSpam'
    raid = 'Raid'
    spam_abuse = 'SpamAbuse'
    scams_fraud = 'ScamsFraud'
    malware = 'Malware'
    harassment = 'Harassment'


class UserReportReason(Enum):
    none = 'NoneSpecified'
    unsolicited_spam = 'UnsolicitedSpam'
    spam_abuse = 'SpamAbuse'
    inappropriate_profile = 'InappropriateProfile'
    impersonation = 'Impersonation'
    ban_evasion = 'BanEvasion'
    underage = 'Underage'


class MemberRemovalIntention(Enum):
    leave = 'Leave'
    kick = 'Kick'
    ban = 'Ban'


class ShardFormat(Enum):
    json = 'json'
    msgpack = 'msgpack'


class AndroidTheme(Enum):
    revolt = 'Revolt'
    light = 'Light'
    pure_black = 'Amoled'
    system = 'None'
    material_you = 'M3Dynamic'


class AndroidProfilePictureShape(Enum):
    sharp = 0
    rounded = 15
    circular = 50


class AndroidMessageReplyStyle(Enum):
    long_press_to_reply = 'None'
    swipe_to_reply = 'SwipeFromEnd'
    double_tap_to_reply = 'DoubleTap'


_CHANGELOG_ENTRIES: dict[int, tuple[datetime, str]] = {
    1: (
        datetime(
            year=2022,
            month=6,
            day=12,
            hour=20,
            minute=39,
            second=16,
            microsecond=674000,
            tzinfo=_UTC,
        ),
        'Secure your account with 2FA',
    ),
    2: (
        datetime(
            year=2023,
            month=2,
            day=23,
            hour=20,
            minute=0,
            tzinfo=_UTC,
        ),
        'In-App Reporting Is Here',
    ),
    3: (
        datetime(
            year=2023,
            month=6,
            day=11,
            hour=15,
            minute=0,
            tzinfo=_UTC,
        ),
        'Usernames are Changing',
    ),
}


class ReviteChangelogEntry(Enum):
    mfa_feature = 1
    iar_reporting_feature = 2
    discriminators_feature = 3

    @property
    def created_at(self) -> datetime:
        return _CHANGELOG_ENTRIES[self.value][0]

    @property
    def title(self) -> str:
        return _CHANGELOG_ENTRIES[self.value][1]


class ReviteNotificationState(Enum):
    all_messages = 'all'
    mentions_only = 'mention'
    none = 'none'
    muted = 'muted'


class ReviteEmojiPack(Enum):
    mutant_remix = 'mutant'
    twemoji = 'twemoji'
    openmoji = 'openmoji'
    noto_emoji = 'noto'


class ReviteBaseTheme(Enum):
    dark = 'dark'
    light = 'light'


class ReviteFont(Enum):
    open_sans = 'Open Sans'
    opendyslexic = 'OpenDyslexic'
    inter = 'Inter'
    atkinson_hyperlegible = 'Atkinson Hyperlegible'
    roboto = 'Roboto'
    noto_sans = 'Noto Sans'
    lato = 'Lato'
    bitter = 'Bitter'
    montserrat = 'Montserrat'
    poppins = 'Poppins'
    raleway = 'Raleway'
    ubuntu = 'Ubuntu'
    comic_neue = 'Comic Neue'
    lexend = 'Lexend'


class ReviteMonoFont(Enum):
    fira_code = 'Fira Code'
    roboto_mono = 'Roboto Mono'
    source_code_pro = 'Source Code Pro'
    space_mono = 'Space Mono'
    ubuntu_mono = 'Ubuntu Mono'
    jetbrains_mono = 'JetBrains Mono'


class Presence(Enum):
    online = 'Online'
    idle = 'Idle'
    focus = 'Focus'
    busy = 'Busy'
    invisible = 'Invisible'


class RelationshipStatus(Enum):
    none = 'None'
    user = 'User'
    friend = 'Friend'
    outgoing = 'Outgoing'
    incoming = 'Incoming'
    blocked = 'Blocked'
    blocked_other = 'BlockedOther'


class ReportStatus(Enum):
    created = 'Created'
    rejected = 'Rejected'
    resolved = 'Resolved'


class ReportedContentType(Enum):
    message = 'Message'
    server = 'Server'
    user = 'User'


__all__ = (
    'EnumMeta',
    'Enum',
    'MFAMethod',
    'AssetMetadataType',
    'ChannelType',
    'ServerActivity',
    'BotUsage',
    'LightspeedContentType',
    'TwitchContentType',
    'BandcampContentType',
    'ImageSize',
    'Language',
    'MessageSort',
    'ContentReportReason',
    'UserReportReason',
    'MemberRemovalIntention',
    'ShardFormat',
    'AndroidTheme',
    'AndroidProfilePictureShape',
    'AndroidMessageReplyStyle',
    'ReviteChangelogEntry',
    'ReviteNotificationState',
    'ReviteEmojiPack',
    'ReviteBaseTheme',
    'ReviteFont',
    'ReviteMonoFont',
    'Presence',
    'RelationshipStatus',
    'ReportStatus',
    'ReportedContentType',
)
