from .const import CONF_KEEP_MAIN_LIGHT as CONF_KEEP_MAIN_LIGHT, DEFAULT_KEEP_MAIN_LIGHT as DEFAULT_KEEP_MAIN_LIGHT, DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from wled import Device as WLEDDevice

class WLEDDataUpdateCoordinator(DataUpdateCoordinator[WLEDDevice]):
    keep_main_light: bool
    config_entry: ConfigEntry
    wled: Incomplete
    unsub: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: ConfigEntry) -> None: ...
    @property
    def has_main_light(self) -> bool: ...
    last_update_success: bool
    def _use_websocket(self) -> None: ...
    async def _async_update_data(self) -> WLEDDevice: ...
