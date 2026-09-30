from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry
from .entity import OpenEVSEEntity as OpenEVSEEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from openevsehttp.__main__ import OpenEVSE as OpenEVSE
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OpenEVSEBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[OpenEVSE], bool | None]

BINARY_SENSOR_TYPES: tuple[OpenEVSEBinarySensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSEBinarySensor(OpenEVSEEntity, BinarySensorEntity):
    entity_description: OpenEVSEBinarySensorDescription
    @property
    @override
    def is_on(self) -> bool | None: ...
