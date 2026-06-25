from . import VistapoolConfigEntry as VistapoolConfigEntry
from .const import PATH_HASCD as PATH_HASCD, PATH_HASCL as PATH_HASCL, PATH_HASHIDRO as PATH_HASHIDRO, PATH_HASIO as PATH_HASIO, PATH_HASPH as PATH_HASPH, PATH_HASRX as PATH_HASRX
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from .entity import VistapoolEntity as VistapoolEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
TANK_MODULE_PATHS: Incomplete

@dataclass(frozen=True, kw_only=True)
class VistapoolBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_path: str
    exists_path: str | tuple[str, ...] | None = ...

BINARY_SENSOR_DESCRIPTIONS: tuple[VistapoolBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VistapoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VistapoolBinarySensor(VistapoolEntity, BinarySensorEntity):
    entity_description: VistapoolBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VistapoolDataUpdateCoordinator, description: VistapoolBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...

class VistapoolDosingTankBinarySensor(VistapoolEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VistapoolDataUpdateCoordinator) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
