import aiohttp
import asyncio
import tarfile
import threading
from .const import BUF_SIZE as BUF_SIZE, LOGGER as LOGGER
from .models import AddonInfo as AddonInfo, AgentBackup as AgentBackup, Folder as Folder
from _typeshed import Incomplete
from collections.abc import AsyncIterator, Callable as Callable, Coroutine
from concurrent.futures import Future
from dataclasses import dataclass
from homeassistant.backup_restore import password_to_key as password_to_key
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.json import JsonObjectType as JsonObjectType, json_loads_object as json_loads_object
from pathlib import Path
from typing import Any, IO, Self

class DecryptError(HomeAssistantError):
    _message: str

class EncryptError(HomeAssistantError):
    _message: str

class UnsupportedSecureTarVersion(DecryptError):
    _message: str

class IncorrectPassword(DecryptError):
    _message: str

class BackupEmpty(DecryptError):
    _message: str

class AbortCipher(HomeAssistantError):
    _message: str

def make_backup_dir(path: Path) -> None: ...
def read_backup(backup_path: Path) -> AgentBackup: ...
def suggested_filename_from_name_date(name: str, date_str: str) -> str: ...
def suggested_filename(backup: AgentBackup) -> str: ...
def validate_password(path: Path, password: str | None) -> bool: ...

class AsyncIteratorReader:
    _aborted: bool
    _hass: Incomplete
    _stream: Incomplete
    _buffer: bytes | None
    _next_future: Future[bytes | None] | None
    _pos: int
    def __init__(self, hass: HomeAssistant, stream: AsyncIterator[bytes]) -> None: ...
    async def _next(self) -> bytes | None: ...
    def abort(self) -> None: ...
    def read(self, n: int = -1, /) -> bytes: ...
    def close(self) -> None: ...

class AsyncIteratorWriter:
    _aborted: bool
    _hass: Incomplete
    _pos: int
    _queue: asyncio.Queue[bytes | None]
    _write_future: Future[bytes | None] | None
    def __init__(self, hass: HomeAssistant) -> None: ...
    def __aiter__(self) -> Self: ...
    async def __anext__(self) -> bytes: ...
    def abort(self) -> None: ...
    def tell(self) -> int: ...
    def write(self, s: bytes, /) -> int: ...

def validate_password_stream(input_stream: IO[bytes], password: str | None) -> None: ...
def decrypt_backup(input_stream: IO[bytes], output_stream: IO[bytes], password: str | None, on_done: Callable[[Exception | None], None], minimum_size: int, nonces: list[bytes]) -> None: ...
def _decrypt_backup(input_tar: tarfile.TarFile, output_tar: tarfile.TarFile, password: str | None) -> None: ...
def encrypt_backup(input_stream: IO[bytes], output_stream: IO[bytes], password: str | None, on_done: Callable[[Exception | None], None], minimum_size: int, nonces: list[bytes]) -> None: ...
def _encrypt_backup(input_tar: tarfile.TarFile, output_tar: tarfile.TarFile, password: str | None, nonces: list[bytes]) -> None: ...

@dataclass(kw_only=True)
class _CipherWorkerStatus:
    done: asyncio.Event
    error: Exception | None = ...
    reader: AsyncIteratorReader
    thread: threading.Thread
    writer: AsyncIteratorWriter

class _CipherBackupStreamer:
    _cipher_func: Callable[[IO[bytes], IO[bytes], str | None, Callable[[Exception | None], None], int, list[bytes]], None]
    _workers: list[_CipherWorkerStatus]
    _backup: Incomplete
    _hass: Incomplete
    _open_stream: Incomplete
    _password: Incomplete
    _nonces: list[bytes]
    def __init__(self, hass: HomeAssistant, backup: AgentBackup, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], password: str | None) -> None: ...
    def size(self) -> int: ...
    def _num_tar_files(self) -> int: ...
    async def open_stream(self) -> AsyncIterator[bytes]: ...
    async def wait(self) -> None: ...

class DecryptedBackupStreamer(_CipherBackupStreamer):
    _cipher_func: Incomplete
    def backup(self) -> AgentBackup: ...

class EncryptedBackupStreamer(_CipherBackupStreamer):
    _nonces: Incomplete
    def __init__(self, hass: HomeAssistant, backup: AgentBackup, open_stream: Callable[[], Coroutine[Any, Any, AsyncIterator[bytes]]], password: str | None) -> None: ...
    _cipher_func: Incomplete
    def backup(self) -> AgentBackup: ...

async def receive_file(hass: HomeAssistant, contents: aiohttp.BodyPartReader, path: Path) -> None: ...
