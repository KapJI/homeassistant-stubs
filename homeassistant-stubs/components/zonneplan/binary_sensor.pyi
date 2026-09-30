from .const import ZONNEPLAN_TIMEZONE as ZONNEPLAN_TIMEZONE
from .coordinator import ZonneplanConfigEntry as ZonneplanConfigEntry, ZonneplanCoordinator as ZonneplanCoordinator
from .entity import ZonneplanEntity as ZonneplanEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_track_time_change as async_track_time_change
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ZonneplanBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[ZonneplanCoordinator], bool | None]

BINARY_SENSORS: tuple[ZonneplanBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ZonneplanConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ZonneplanBinarySensor(ZonneplanEntity, BinarySensorEntity):
    entity_description: ZonneplanBinarySensorEntityDescription
    @override
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_hour_changed(self, now: datetime) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
