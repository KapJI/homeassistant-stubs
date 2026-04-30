from .base import BaseTemplateExtension as BaseTemplateExtension, TemplateFunction as TemplateFunction
from _typeshed import Incomplete
from homeassistant.helpers.template import TemplateEnvironment as TemplateEnvironment
from homeassistant.helpers.template.helpers import forgiving_boolean as forgiving_boolean, raise_no_default as raise_no_default
from typing import Any

_SENTINEL: Incomplete

class TypeCastExtension(BaseTemplateExtension):
    def __init__(self, environment: TemplateEnvironment) -> None: ...
    @staticmethod
    def forgiving_float(value: Any, default: Any = ...) -> Any: ...
    @staticmethod
    def forgiving_int(value: Any, default: Any = ..., base: int = 10) -> Any: ...
    @staticmethod
    def is_number(value: Any) -> bool: ...
    @staticmethod
    def is_string_like(value: Any) -> bool: ...
