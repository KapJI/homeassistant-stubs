import attr
from .const import REDACTED as REDACTED
from _typeshed import Incomplete
from collections.abc import Iterable, Mapping
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from typing import Any, overload

@overload
def async_redact_data(data: Mapping, to_redact: Iterable[Any]) -> dict: ...
@overload
def async_redact_data[_T](data: _T, to_redact: Iterable[Any]) -> _T: ...

_INTERNAL_DEVICE_ENTRY_ATTRIBUTES: Incomplete

def _device_entry_filter(a: attr.Attribute, _: Any) -> bool: ...
@callback
def device_entry_as_dict(entry: DeviceEntry) -> dict[str, Any]: ...
def _entity_entry_filter(a: attr.Attribute, _: Any) -> bool: ...
@callback
def entity_entry_as_dict(entry: RegistryEntry) -> dict[str, Any]: ...
