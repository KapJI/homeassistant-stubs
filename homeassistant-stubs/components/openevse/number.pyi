from .const import DOMAIN as DOMAIN
from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry, OpenEVSEDataUpdateCoordinator as OpenEVSEDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, EntityCategory as EntityCategory, UnitOfElectricCurrent as UnitOfElectricCurrent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from openevsehttp.__main__ import OpenEVSE as OpenEVSE
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OpenEVSENumberDescription(NumberEntityDescription):
    value_fn: Callable[[OpenEVSE], float]
    min_value_fn: Callable[[OpenEVSE], float]
    max_value_fn: Callable[[OpenEVSE], float]
    set_value_fn: Callable[[OpenEVSE, float], Awaitable[Any]]

NUMBER_TYPES: tuple[OpenEVSENumberDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSENumber(CoordinatorEntity[OpenEVSEDataUpdateCoordinator], NumberEntity):
    _attr_has_entity_name: bool
    entity_description: OpenEVSENumberDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OpenEVSEDataUpdateCoordinator, description: OpenEVSENumberDescription, identifier: str, unique_id: str | None) -> None: ...
    @property
    def native_value(self) -> float: ...
    @property
    def native_min_value(self) -> float: ...
    @property
    def native_max_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
