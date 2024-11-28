from . import NordPoolConfigEntry as NordPoolConfigEntry
from .const import CONF_AREAS as CONF_AREAS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.const import CONF_CURRENCY as CONF_CURRENCY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pynordpool import DeliveryPeriodData

class NordPoolDataUpdateCoordinator(DataUpdateCoordinator[DeliveryPeriodData]):
    config_entry: NordPoolConfigEntry
    client: Incomplete
    unsub: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: NordPoolConfigEntry) -> None: ...
    def get_next_interval(self, now: datetime) -> datetime: ...
    async def async_shutdown(self) -> None: ...
    async def fetch_data(self, now: datetime) -> None: ...
