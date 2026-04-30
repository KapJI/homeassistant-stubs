from .base import BaseTemplateExtension as BaseTemplateExtension, TemplateFunction as TemplateFunction
from _typeshed import Incomplete
from homeassistant.helpers.template import TemplateEnvironment as TemplateEnvironment
from homeassistant.helpers.template.helpers import raise_no_default as raise_no_default
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from typing import Any

_LOGGER: Incomplete
_SENTINEL: Incomplete
_ORJSON_PASSTHROUGH_OPTIONS: Incomplete

class SerializationExtension(BaseTemplateExtension):
    def __init__(self, environment: TemplateEnvironment) -> None: ...
    @staticmethod
    def struct_pack(value: Any | None, format_string: str) -> bytes | None: ...
    @staticmethod
    def struct_unpack(value: bytes, format_string: str, offset: int = 0) -> Any | None: ...
    @staticmethod
    def from_json(value: Any, default: Any = ...) -> Any: ...
    @staticmethod
    def to_json(value: Any, ensure_ascii: bool = False, pretty_print: bool = False, sort_keys: bool = False) -> str: ...
    @staticmethod
    def from_hex(value: str) -> bytes: ...

def _to_json_default(obj: Any) -> None: ...
