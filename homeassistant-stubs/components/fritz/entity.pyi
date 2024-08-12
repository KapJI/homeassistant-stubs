from .const import DEFAULT_DEVICE_NAME as DEFAULT_DEVICE_NAME, DOMAIN as DOMAIN
from .coordinator import AvmWrapper as AvmWrapper, FritzDevice as FritzDevice
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from fritzconnection.lib.fritzstatus import FritzStatus as FritzStatus
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class FritzDeviceBase(CoordinatorEntity[AvmWrapper]):
    _avm_wrapper: Incomplete
    _mac: Incomplete
    _name: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device: FritzDevice) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def ip_address(self) -> str | None: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def hostname(self) -> str | None: ...
    async def async_process_update(self) -> None: ...
    async def async_on_demand_update(self) -> None: ...

class FritzBoxBaseEntity:
    _avm_wrapper: Incomplete
    _device_name: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_name: str) -> None: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...

@dataclass(frozen=True, kw_only=True)
class FritzEntityDescription(EntityDescription):
    value_fn: Callable[[FritzStatus, Any], Any] | None
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., value_fn) -> None: ...

class FritzBoxBaseCoordinatorEntity(CoordinatorEntity[AvmWrapper]):
    entity_description: FritzEntityDescription
    _attr_has_entity_name: bool
    _device_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_name: str, description: FritzEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
