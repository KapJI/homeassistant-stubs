from .const import CONF_CANDLE_LIGHT_MINUTES as CONF_CANDLE_LIGHT_MINUTES, CONF_DIASPORA as CONF_DIASPORA, CONF_HAVDALAH_OFFSET_MINUTES as CONF_HAVDALAH_OFFSET_MINUTES, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import date as Date
from hdate import HDate
from hdate.zmanim import Zmanim
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_LANGUAGE as CONF_LANGUAGE, CONF_LOCATION as CONF_LOCATION, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sun import get_astral_event_date as get_astral_event_date
from typing import Any

_LOGGER: Incomplete
INFO_SENSORS: tuple[SensorEntityDescription, ...]
TIME_SENSORS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JewishCalendarSensor(SensorEntity):
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _location: Incomplete
    _hebrew: Incomplete
    _candle_lighting_offset: Incomplete
    _havdalah_offset: Incomplete
    _diaspora: Incomplete
    _holiday_attrs: Incomplete
    def __init__(self, entry_id: str, data: dict[str, Any], description: SensorEntityDescription) -> None: ...
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
    def make_zmanim(self, date: Date) -> Zmanim: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    def get_state(self, daytime_date: HDate, after_shkia_date: HDate, after_tzais_date: HDate) -> Any | None: ...

class JewishCalendarTimeSensor(JewishCalendarSensor):
    _attr_device_class: Incomplete
    def get_state(self, daytime_date: HDate, after_shkia_date: HDate, after_tzais_date: HDate) -> Any | None: ...
