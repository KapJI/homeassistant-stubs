import datetime as dt
from .entity import JewishCalendarConfigEntry as JewishCalendarConfigEntry, JewishCalendarEntity as JewishCalendarEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from hdate.zmanim import Zmanim as Zmanim
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class JewishCalendarBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on: Callable[[Zmanim], Callable[[dt.datetime], bool]]

BINARY_SENSORS: tuple[JewishCalendarBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: JewishCalendarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class JewishCalendarBinarySensor(JewishCalendarEntity, BinarySensorEntity):
    _attr_entity_category: Incomplete
    entity_description: JewishCalendarBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
    def _update_times(self, zmanim: Zmanim) -> list[dt.datetime | None]: ...
