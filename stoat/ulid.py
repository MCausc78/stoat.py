from __future__ import annotations

from os import urandom
from time import time
import typing

# https://github.com/mdomke/python-ulid/blob/main/ulid/__init__.py
# https://github.com/mdomke/python-ulid/blob/main/ulid/base32.py

_CROCKFORD_BASE32_ALPHABET: typing.Final[str] = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
_LUT: typing.Final[list[int]] = [
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0x00,
    0x01,
    0x02,
    0x03,
    0x04,
    0x05,
    0x06,
    0x07,
    0x08,
    0x09,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0x0A,
    0x0B,
    0x0C,
    0x0D,
    0x0E,
    0x0F,
    0x10,
    0x11,
    0xFF,
    0x12,
    0x13,
    0xFF,
    0x14,
    0x15,
    0xFF,
    0x16,
    0x17,
    0x18,
    0x19,
    0x1A,
    0xFF,
    0x1B,
    0x1C,
    0x1D,
    0x1E,
    0x1F,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0x0A,
    0x0B,
    0x0C,
    0x0D,
    0x0E,
    0x0F,
    0x10,
    0x11,
    0xFF,
    0x12,
    0x13,
    0xFF,
    0x14,
    0x15,
    0xFF,
    0x16,
    0x17,
    0x18,
    0x19,
    0x1A,
    0xFF,
    0x1B,
    0x1C,
    0x1D,
    0x1E,
    0x1F,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
]


def _ulid_timestamp(v: bytes, /) -> float:
    return int.from_bytes(_ulid_decode_timestamp(v)[:6], byteorder='big') / 1000


def _ulid_decode_timestamp(v: bytes, /) -> bytes:
    return bytes(
        [
            ((_LUT[v[0]] << 5) | _LUT[v[1]]) & 0xFF,
            ((_LUT[v[2]] << 3) | (_LUT[v[3]] >> 2)) & 0xFF,
            ((_LUT[v[3]] << 6) | (_LUT[v[4]] << 1) | (_LUT[v[5]] >> 4)) & 0xFF,
            ((_LUT[v[5]] << 4) | (_LUT[v[6]] >> 1)) & 0xFF,
            ((_LUT[v[6]] << 7) | (_LUT[v[7]] << 2) | (_LUT[v[8]] >> 3)) & 0xFF,
            ((_LUT[v[8]] << 5) | (_LUT[v[9]])) & 0xFF,
        ]
    )


def _ulid_encode(v: bytes, /) -> str:
    return _ulid_encode_timestamp(v[:6]) + _ulid_encode_randomness(v[6:])


def _ulid_encode_timestamp(v: bytes, /) -> str:
    return ''.join(
        [
            _CROCKFORD_BASE32_ALPHABET[(v[0] & 224) >> 5],
            _CROCKFORD_BASE32_ALPHABET[(v[0] & 31)],
            _CROCKFORD_BASE32_ALPHABET[(v[1] & 248) >> 3],
            _CROCKFORD_BASE32_ALPHABET[((v[1] & 7) << 2) | ((v[2] & 192) >> 6)],
            _CROCKFORD_BASE32_ALPHABET[((v[2] & 62) >> 1)],
            _CROCKFORD_BASE32_ALPHABET[((v[2] & 1) << 4) | ((v[3] & 240) >> 4)],
            _CROCKFORD_BASE32_ALPHABET[((v[3] & 15) << 1) | ((v[4] & 128) >> 7)],
            _CROCKFORD_BASE32_ALPHABET[(v[4] & 124) >> 2],
            _CROCKFORD_BASE32_ALPHABET[((v[4] & 3) << 3) | ((v[5] & 224) >> 5)],
            _CROCKFORD_BASE32_ALPHABET[(v[5] & 31)],
        ]
    )


def _ulid_encode_randomness(v: bytes, /) -> str:
    return ''.join(
        [
            _CROCKFORD_BASE32_ALPHABET[(v[0] & 248) >> 3],
            _CROCKFORD_BASE32_ALPHABET[((v[0] & 7) << 2) | ((v[1] & 192) >> 6)],
            _CROCKFORD_BASE32_ALPHABET[(v[1] & 62) >> 1],
            _CROCKFORD_BASE32_ALPHABET[((v[1] & 1) << 4) | ((v[2] & 240) >> 4)],
            _CROCKFORD_BASE32_ALPHABET[((v[2] & 15) << 1) | ((v[3] & 128) >> 7)],
            _CROCKFORD_BASE32_ALPHABET[(v[3] & 124) >> 2],
            _CROCKFORD_BASE32_ALPHABET[((v[3] & 3) << 3) | ((v[4] & 224) >> 5)],
            _CROCKFORD_BASE32_ALPHABET[(v[4] & 31)],
            _CROCKFORD_BASE32_ALPHABET[(v[5] & 248) >> 3],
            _CROCKFORD_BASE32_ALPHABET[((v[5] & 7) << 2) | ((v[6] & 192) >> 6)],
            _CROCKFORD_BASE32_ALPHABET[(v[6] & 62) >> 1],
            _CROCKFORD_BASE32_ALPHABET[((v[6] & 1) << 4) | ((v[7] & 240) >> 4)],
            _CROCKFORD_BASE32_ALPHABET[((v[7] & 15) << 1) | ((v[8] & 128) >> 7)],
            _CROCKFORD_BASE32_ALPHABET[(v[8] & 124) >> 2],
            _CROCKFORD_BASE32_ALPHABET[((v[8] & 3) << 3) | ((v[9] & 224) >> 5)],
            _CROCKFORD_BASE32_ALPHABET[(v[9] & 31)],
        ]
    )


def _ulid_new() -> str:
    timestamp = int(time() * 1000).to_bytes(6, byteorder='big')
    randomness = urandom(10)
    return _ulid_encode(timestamp + randomness)


__all__ = (
    '_LUT',
    '_ulid_timestamp',
    '_ulid_decode_timestamp',
    '_ulid_encode',
    '_ulid_encode_timestamp',
    '_ulid_encode_randomness',
    '_ulid_new',
)
