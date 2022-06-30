from .const import CONF_FROM as CONF_FROM, CONF_TIME as CONF_TIME, CONF_TO as CONF_TO, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import date
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_WEEKDAY as CONF_WEEKDAY, WEEKDAYS as WEEKDAYS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util import dt as dt
from pytrafikverket.trafikverket_ferry import FerryStop as FerryStop
from typing import Any

_LOGGER: Incomplete
TIME_BETWEEN_UPDATES: Incomplete

def next_weekday(fromdate: date, weekday: int) -> date: ...
def next_departuredate(departure: list[str]) -> date: ...

class TVDataUpdateCoordinator(DataUpdateCoordinator):
    _ferry_api: Incomplete
    _from: Incomplete
    _to: Incomplete
    _time: Incomplete
    _weekdays: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
