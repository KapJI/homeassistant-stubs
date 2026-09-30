from .const import LOGGER as LOGGER
from .coordinator import VitesyConfigEntry as VitesyConfigEntry, VitesyDataUpdateCoordinator as VitesyDataUpdateCoordinator
from .entity import VitesyEntity as VitesyEntity
from _typeshed import Incomplete
from aiovitesy.api import VitesyDevice as VitesyDevice
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

def _status_flag(reading_id: str) -> Callable[[VitesyDevice], bool | None]: ...

@dataclass(frozen=True, kw_only=True)
class VitesyBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[VitesyDevice], bool | None]

BINARY_SENSORS: tuple[VitesyBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VitesyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VitesyBinarySensor(VitesyEntity, BinarySensorEntity):
    entity_description: VitesyBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VitesyDataUpdateCoordinator, device_id: str, description: VitesyBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
