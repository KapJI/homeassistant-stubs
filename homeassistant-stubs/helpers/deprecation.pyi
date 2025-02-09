import functools
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from enum import EnumType, IntEnum, IntFlag, StrEnum, _EnumDict
from typing import Any, NamedTuple

def deprecated_substitute[_ObjectT: object](substitute_name: str) -> Callable[[Callable[[_ObjectT], Any]], Callable[[_ObjectT], Any]]: ...
def get_deprecated(config: dict[str, Any], new_name: str, old_name: str, default: Any | None = None) -> Any | None: ...
def deprecated_class[**_P, _R](replacement: str, *, breaks_in_ha_version: str | None = None) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]: ...
def deprecated_function[**_P, _R](replacement: str, *, breaks_in_ha_version: str | None = None) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]: ...
def _print_deprecation_warning(obj: Any, replacement: str, description: str, verb: str, breaks_in_ha_version: str | None) -> None: ...
def _print_deprecation_warning_internal(obj_name: str, module_name: str, replacement: str, description: str, verb: str, breaks_in_ha_version: str | None, *, log_when_no_integration_is_found: bool) -> None: ...
def _print_deprecation_warning_internal_impl(obj_name: str, module_name: str, replacement: str, description: str, verb: str, breaks_in_ha_version: str | None, *, log_when_no_integration_is_found: bool) -> None: ...

class DeprecatedConstant(NamedTuple):
    value: Any
    replacement: str
    breaks_in_ha_version: str | None

class DeprecatedConstantEnum(NamedTuple):
    enum: StrEnum | IntEnum | IntFlag
    breaks_in_ha_version: str | None

class DeprecatedAlias(NamedTuple):
    value: Any
    replacement: str
    breaks_in_ha_version: str | None

class DeferredDeprecatedAlias:
    breaks_in_ha_version: Incomplete
    replacement: Incomplete
    _value_fn: Incomplete
    def __init__(self, value_fn: Callable[[], Any], replacement: str, breaks_in_ha_version: str | None) -> None: ...
    @functools.cached_property
    def value(self) -> Any: ...

_PREFIX_DEPRECATED: str

def check_if_deprecated_constant(name: str, module_globals: dict[str, Any]) -> Any: ...
def dir_with_deprecated_constants(module_globals_keys: list[str]) -> list[str]: ...
def all_with_deprecated_constants(module_globals: dict[str, Any]) -> list[str]: ...

class EnumWithDeprecatedMembers(EnumType):
    def __new__(mcs, cls: str, bases: tuple[type, ...], classdict: _EnumDict, *, deprecated: dict[str, tuple[str, str]], **kwds: Any) -> Any: ...
    def __getattribute__(cls, name: str) -> Any: ...
