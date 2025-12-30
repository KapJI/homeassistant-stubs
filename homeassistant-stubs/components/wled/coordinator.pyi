from .const import CONF_KEEP_MAIN_LIGHT as CONF_KEEP_MAIN_LIGHT, DEFAULT_KEEP_MAIN_LIGHT as DEFAULT_KEEP_MAIN_LIGHT, DOMAIN as DOMAIN, LOGGER as LOGGER, RELEASES_SCAN_INTERVAL as RELEASES_SCAN_INTERVAL, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from wled import Device as WLEDDevice, Releases

type WLEDConfigEntry = ConfigEntry[WLEDDataUpdateCoordinator]
def normalize_mac_address(mac: str) -> str: ...

class WLEDDataUpdateCoordinator(DataUpdateCoordinator[WLEDDevice]):
    keep_main_light: bool
    config_entry: WLEDConfigEntry
    wled: Incomplete
    unsub: CALLBACK_TYPE | None
    config_mac_address: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: WLEDConfigEntry) -> None: ...
    @property
    def has_main_light(self) -> bool: ...
    last_update_success: bool
    @callback
    def _use_websocket(self) -> None: ...
    async def _async_update_data(self) -> WLEDDevice: ...

class WLEDReleasesDataUpdateCoordinator(DataUpdateCoordinator[Releases]):
    wled: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> Releases: ...
