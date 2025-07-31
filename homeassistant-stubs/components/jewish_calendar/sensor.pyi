import datetime as dt
from .entity import JewishCalendarConfigEntry as JewishCalendarConfigEntry, JewishCalendarEntity as JewishCalendarEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from hdate import HDateInfo as HDateInfo, Zmanim as Zmanim
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class JewishCalendarBaseSensorDescription(SensorEntityDescription):
    value_fn: Callable | None
    next_update_fn: Callable[[Zmanim], dt.datetime | None] | None

@dataclass(frozen=True, kw_only=True)
class JewishCalendarSensorDescription(JewishCalendarBaseSensorDescription):
    value_fn: Callable[[HDateInfo], str | int]
    attr_fn: Callable[[HDateInfo], dict[str, str]] | None = ...
    options_fn: Callable[[bool], list[str]] | None = ...
    next_update_fn: Callable[[Zmanim], dt.datetime | None] | None = ...

@dataclass(frozen=True, kw_only=True)
class JewishCalendarTimestampSensorDescription(JewishCalendarBaseSensorDescription):
    value_fn: Callable[[HDateInfo, Callable[[dt.date], Zmanim]], dt.datetime | None] | None = ...
    next_update_fn: Callable[[Zmanim], dt.datetime | None] | None = ...

INFO_SENSORS: tuple[JewishCalendarSensorDescription, ...]
TIME_SENSORS: tuple[JewishCalendarTimestampSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: JewishCalendarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class JewishCalendarBaseSensor(JewishCalendarEntity, SensorEntity):
    _attr_entity_category: Incomplete
    entity_description: JewishCalendarBaseSensorDescription
    def _update_times(self, zmanim: Zmanim) -> list[dt.datetime | None]: ...
    def get_dateinfo(self, now: dt.datetime | None = None) -> HDateInfo: ...

class JewishCalendarSensor(JewishCalendarBaseSensor):
    entity_description: JewishCalendarSensorDescription
    _attr_options: Incomplete
    def __init__(self, config_entry: JewishCalendarConfigEntry, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> str | int | dt.datetime | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...

class JewishCalendarTimeSensor(JewishCalendarBaseSensor):
    _attr_device_class: Incomplete
    entity_description: JewishCalendarTimestampSensorDescription
    @property
    def native_value(self) -> dt.datetime | None: ...
