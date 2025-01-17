import dataclasses
from typing import Any, dataclass_transform

def _class_fields(cls, kw_only: bool) -> list[tuple[str, Any, Any]]: ...

@dataclass_transform(field_specifiers=(dataclasses.field, dataclasses.Field), frozen_default=True, kw_only_default=True)
class FrozenOrThawed(type):
    def _make_dataclass(cls, name: str, bases: tuple[type, ...], kw_only: bool) -> None: ...
    def __new__(mcs, name: str, bases: tuple[type, ...], namespace: dict[Any, Any], frozen_or_thawed: bool = False, **kwargs: Any) -> Any: ...
    def __init__(cls, name: str, bases: tuple[type, ...], namespace: dict[Any, Any], **kwargs: Any) -> None: ...
