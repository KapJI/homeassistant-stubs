from .coordinator import LibrenmsConfigEntry as LibrenmsConfigEntry, LibrenmsDataUpdateCoordinator as LibrenmsDataUpdateCoordinator
from .entity import LibrenmsDeviceEntity as LibrenmsDeviceEntity
from _typeshed import Incomplete
from aiolibrenms.devices.models import LibrenmsDeviceInfo as LibrenmsDeviceInfo
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LibrenmsDeviceBinarySensorEntityDescription(BinarySensorEntityDescription):
    value: Callable[[LibrenmsDeviceInfo], bool]
    is_suitable: Callable[[LibrenmsDeviceInfo], bool] = ...

DEVICE_SENSOR_TYPES: tuple[LibrenmsDeviceBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LibrenmsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LibrenmsDeviceBinarySensorEntity(LibrenmsDeviceEntity, BinarySensorEntity):
    entity_description: LibrenmsDeviceBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LibrenmsDataUpdateCoordinator, description: LibrenmsDeviceBinarySensorEntityDescription, device_id: int) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
