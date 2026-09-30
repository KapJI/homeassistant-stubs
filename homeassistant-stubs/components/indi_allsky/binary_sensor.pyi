from .coordinator import IndiAllSkyConfigEntry as IndiAllSkyConfigEntry, IndiAllSkyData as IndiAllSkyData, IndiAllSkyDataUpdateCoordinator as IndiAllSkyDataUpdateCoordinator
from .entity import IndiAllSkyEntity as IndiAllSkyEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IndiAllSkyBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[IndiAllSkyData], bool | None]

BINARY_SENSOR_DESCRIPTIONS: tuple[IndiAllSkyBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: IndiAllSkyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IndiAllSkyBinarySensor(IndiAllSkyEntity, BinarySensorEntity):
    entity_description: IndiAllSkyBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IndiAllSkyDataUpdateCoordinator, entry: IndiAllSkyConfigEntry, description: IndiAllSkyBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
