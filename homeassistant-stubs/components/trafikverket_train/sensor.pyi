from datetime import date, datetime, time
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, CONF_WEEKDAY as CONF_WEEKDAY, WEEKDAYS as WEEKDAYS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.dt import as_utc as as_utc, get_time_zone as get_time_zone
from pytrafikverket import TrafikverketTrain
from pytrafikverket.trafikverket_train import TrainStop as TrainStop
from typing import Any

_LOGGER: Any
CONF_TRAINS: str
CONF_FROM: str
CONF_TO: str
CONF_TIME: str
ATTR_DEPARTURE_STATE: str
ATTR_CANCELED: str
ATTR_DELAY_TIME: str
ATTR_PLANNED_TIME: str
ATTR_ESTIMATED_TIME: str
ATTR_ACTUAL_TIME: str
ATTR_OTHER_INFORMATION: str
ATTR_DEVIATIONS: str
ICON: str
SCAN_INTERVAL: Any
STOCKHOLM_TIMEZONE: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
def next_weekday(fromdate: date, weekday: int) -> date: ...
def next_departuredate(departure: list[str]) -> date: ...
def _to_iso_format(traintime: datetime) -> str: ...

class TrainSensor(SensorEntity):
    _attr_icon: Any
    _attr_device_class: Any
    _train_api: Any
    _attr_name: Any
    _from_station: Any
    _to_station: Any
    _weekday: Any
    _time: Any
    def __init__(self, train_api: TrafikverketTrain, name: str, from_station: str, to_station: str, weekday: list, departuretime: time) -> None: ...
    _attr_available: bool
    _attr_native_value: Any
    _attr_extra_state_attributes: Any
    async def async_update(self) -> None: ...
    def _update_attributes(self, state: TrainStop) -> None: ...
