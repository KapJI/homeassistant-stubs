from .const import CONF_FROM as CONF_FROM, CONF_TIME as CONF_TIME, CONF_TO as CONF_TO, DOMAIN as DOMAIN
from .util import create_unique_id as create_unique_id
from _typeshed import Incomplete
from datetime import date, datetime, time
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_WEEKDAY as CONF_WEEKDAY, WEEKDAYS as WEEKDAYS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import dt as dt
from pytrafikverket import TrafikverketTrain as TrafikverketTrain
from pytrafikverket.trafikverket_train import StationInfo as StationInfo, TrainStop as TrainStop

_LOGGER: Incomplete
ATTR_DEPARTURE_STATE: str
ATTR_CANCELED: str
ATTR_DELAY_TIME: str
ATTR_PLANNED_TIME: str
ATTR_ESTIMATED_TIME: str
ATTR_ACTUAL_TIME: str
ATTR_OTHER_INFORMATION: str
ATTR_DEVIATIONS: str
ICON: str
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def next_weekday(fromdate: date, weekday: int) -> date: ...
def next_departuredate(departure: list[str]) -> date: ...
def _to_iso_format(traintime: datetime) -> str: ...

class TrainSensor(SensorEntity):
    _attr_icon: Incomplete
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _train_api: Incomplete
    _from_station: Incomplete
    _to_station: Incomplete
    _weekday: Incomplete
    _time: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, train_api: TrafikverketTrain, name: str, from_station: StationInfo, to_station: StationInfo, weekday: list, departuretime: Union[time, None], entry_id: str) -> None: ...
    _attr_available: bool
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    async def async_update(self) -> None: ...
    def _update_attributes(self, state: TrainStop) -> None: ...
