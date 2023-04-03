import json
import orjson
from .file import WriteError as WriteError
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from os import PathLike
from typing import Any

_SENTINEL: Incomplete
_LOGGER: Incomplete
JsonValueType: Incomplete
JsonArrayType = list[JsonValueType]
JsonObjectType = dict[str, JsonValueType]
JSON_ENCODE_EXCEPTIONS: Incomplete
JSON_DECODE_EXCEPTIONS: Incomplete

class SerializationError(HomeAssistantError): ...

json_loads: Callable[[bytes | bytearray | memoryview | str], JsonValueType]
json_loads = orjson.loads

def json_loads_array(__obj: bytes | bytearray | memoryview | str) -> JsonArrayType: ...
def json_loads_object(__obj: bytes | bytearray | memoryview | str) -> JsonObjectType: ...
def load_json(filename: str | PathLike, default: JsonValueType = ...) -> JsonValueType: ...
def load_json_array(filename: str | PathLike, default: JsonArrayType = ...) -> JsonArrayType: ...
def load_json_object(filename: str | PathLike, default: JsonObjectType = ...) -> JsonObjectType: ...
def save_json(filename: str, data: list | dict, private: bool = ..., *, encoder: type[json.JSONEncoder] | None = ..., atomic_writes: bool = ...) -> None: ...
def format_unserializable_data(data: dict[str, Any]) -> str: ...
def find_paths_unserializable_data(bad_data: Any, *, dump: Callable[[Any], str] = ...) -> dict[str, Any]: ...
