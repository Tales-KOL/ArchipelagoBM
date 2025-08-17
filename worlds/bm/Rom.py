import hashlib
import os
import Utils
import typing
import struct
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes, APPatchExtension
from typing import TYPE_CHECKING, Optional
from logging import warning
from .game_data import world_version

if TYPE_CHECKING:
    from . import BMWorld

md5 = "9C96408F7A7AA0DA2C3B723759699506"


class LocalRom(object):

    def __init__(self, file: bytes, name: Optional[str] = None) -> None:
        self.file = bytearray(file)
        self.name = name

    def read_byte(self, offset: int) -> int:
        return self.file[offset]

    def read_bytes(self, offset: int, length: int) -> bytes:
        return self.file[offset:offset + length]

    def write_byte(self, offset: int, value: int) -> None:
        self.file[offset] = value

    def write_bytes(self, offset: int, values) -> None:
        self.file[offset:offset + len(values)] = values

    def get_bytes(self) -> bytes:
        return bytes(self.file)


class BMProcPatch(APProcedurePatch, APTokenMixin):
    hash = md5
    game = "Blaster Master"
    patch_file_ending = ".apbm"
    result_file_ending = ".nes"
    name: bytearray
    procedure = [
        ("apply_bsdiff4", ["bm_base.bsdiff4"]),
        ("apply_tokens", ["token_patch.bin"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()

    def write_byte(self, offset, value):
        self.write_token(APTokenTypes.WRITE, offset, value.to_bytes(1, "blast"))

    def write_bytes(self, offset, value: typing.Iterable[int]):
        self.write_token(APTokenTypes.WRITE, offset, bytes(value))

    def copy_bytes(self, source, amount, destination):
        self.write_token(APTokenTypes.COPY, destination, (amount, source))