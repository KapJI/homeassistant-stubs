from .const import DOMAIN as DOMAIN
from .ics import InvalidIcsException as InvalidIcsException, parse_calendar as parse_calendar
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from ical.calendar import Calendar

type RemoteCalendarConfigEntry = ConfigEntry[RemoteCalendarDataUpdateCoordinator]
_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete

class RemoteCalendarDataUpdateCoordinator(DataUpdateCoordinator[Calendar]):
    config_entry: RemoteCalendarConfigEntry
    ics: str
    _client: Incomplete
    _url: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RemoteCalendarConfigEntry) -> None: ...
    async def _async_update_data(self) -> Calendar: ...
