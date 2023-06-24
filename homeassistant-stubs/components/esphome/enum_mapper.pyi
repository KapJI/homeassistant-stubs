from _typeshed import Incomplete
from aioesphomeapi import APIIntEnum
from typing import Generic, TypeVar, overload

_EnumT = TypeVar('_EnumT', bound=APIIntEnum)
_ValT = TypeVar('_ValT')

class EsphomeEnumMapper(Generic[_EnumT, _ValT]):
    _mapping: Incomplete
    _inverse: Incomplete
    def __init__(self, mapping: dict[_EnumT, _ValT]) -> None: ...
    @overload
    def from_esphome(self, value: _EnumT) -> _ValT: ...
    @overload
    def from_esphome(self, value: _EnumT | None) -> _ValT | None: ...
    def from_hass(self, value: _ValT) -> _EnumT: ...
