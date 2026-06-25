from .coordinator import YotoConfigEntry as YotoConfigEntry, YotoDataUpdateCoordinator as YotoDataUpdateCoordinator
from .entity import YotoPlayerEntity as YotoPlayerEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override
from yoto_api import YotoPlayer as YotoPlayer

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class YotoBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[YotoPlayer], bool | None]

BINARY_SENSORS: tuple[YotoBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: YotoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class YotoBinarySensor(YotoPlayerEntity, BinarySensorEntity):
    entity_description: YotoBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: YotoDataUpdateCoordinator, player: YotoPlayer, description: YotoBinarySensorEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
