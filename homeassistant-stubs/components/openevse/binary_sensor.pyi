from .const import DOMAIN as DOMAIN
from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry, OpenEVSEDataUpdateCoordinator as OpenEVSEDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from openevsehttp.__main__ import OpenEVSE as OpenEVSE
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OpenEVSEBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[OpenEVSE], bool | None]

BINARY_SENSOR_TYPES: tuple[OpenEVSEBinarySensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSEBinarySensor(CoordinatorEntity[OpenEVSEDataUpdateCoordinator], BinarySensorEntity):
    _attr_has_entity_name: bool
    entity_description: OpenEVSEBinarySensorDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OpenEVSEDataUpdateCoordinator, description: OpenEVSEBinarySensorDescription, identifier: str, unique_id: str | None) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
