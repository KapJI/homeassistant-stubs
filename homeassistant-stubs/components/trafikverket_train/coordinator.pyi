from . import TVTrainConfigEntry as TVTrainConfigEntry
from .const import CONF_FILTER_PRODUCT as CONF_FILTER_PRODUCT, CONF_FROM as CONF_FROM, CONF_TIME as CONF_TIME, CONF_TO as CONF_TO, DOMAIN as DOMAIN
from .util import next_departuredate as next_departuredate
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import datetime
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_WEEKDAY as CONF_WEEKDAY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pytrafikverket.models import StationInfoModel as StationInfoModel, TrainStopModel as TrainStopModel

@dataclass
class TrainData:
    departure_time: datetime | None
    departure_state: str
    cancelled: bool | None
    delayed_time: int | None
    planned_time: datetime | None
    estimated_time: datetime | None
    actual_time: datetime | None
    other_info: str | None
    deviation: str | None
    product_filter: str | None
    departure_time_next: datetime | None
    departure_time_next_next: datetime | None
    def __init__(self, departure_time, departure_state, cancelled, delayed_time, planned_time, estimated_time, actual_time, other_info, deviation, product_filter, departure_time_next, departure_time_next_next) -> None: ...

_LOGGER: Incomplete
TIME_BETWEEN_UPDATES: Incomplete

def _get_as_utc(date_value: datetime | None) -> datetime | None: ...
def _get_as_joined(information: list[str] | None) -> str | None: ...

class TVDataUpdateCoordinator(DataUpdateCoordinator[TrainData]):
    config_entry: TVTrainConfigEntry
    from_station: StationInfoModel
    to_station: StationInfoModel
    _train_api: Incomplete
    _time: Incomplete
    _weekdays: Incomplete
    _filter_product: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> TrainData: ...
