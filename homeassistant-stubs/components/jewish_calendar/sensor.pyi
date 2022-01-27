from . import DOMAIN as DOMAIN
from datetime import date as Date
from hdate import HDate
from hdate.zmanim import Zmanim
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.sun import get_astral_event_date as get_astral_event_date
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Any
DATA_SENSORS: Any
TIME_SENSORS: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class JewishCalendarSensor(SensorEntity):
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    _location: Any
    _hebrew: Any
    _candle_lighting_offset: Any
    _havdalah_offset: Any
    _diaspora: Any
    _holiday_attrs: Any
    def __init__(self, data: dict[str, Union[str, bool, int, float]], description: SensorEntityDescription) -> None: ...
    _attr_native_value: Any
    async def async_update(self) -> None: ...
    def make_zmanim(self, date: Date) -> Zmanim: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    def get_state(self, daytime_date: HDate, after_shkia_date: HDate, after_tzais_date: HDate) -> Union[Any, None]: ...

class JewishCalendarTimeSensor(JewishCalendarSensor):
    _attr_device_class: Any
    def get_state(self, daytime_date: HDate, after_shkia_date: HDate, after_tzais_date: HDate) -> Union[Any, None]: ...
