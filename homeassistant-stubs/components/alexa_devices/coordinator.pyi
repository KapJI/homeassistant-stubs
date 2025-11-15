from .const import CONF_LOGIN_DATA as CONF_LOGIN_DATA, DOMAIN as DOMAIN, _LOGGER as _LOGGER
from _typeshed import Incomplete
from aioamazondevices.structures import AmazonDevice
from aiohttp import ClientSession as ClientSession
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

SCAN_INTERVAL: int
type AmazonConfigEntry = ConfigEntry[AmazonDevicesCoordinator]

class AmazonDevicesCoordinator(DataUpdateCoordinator[dict[str, AmazonDevice]]):
    config_entry: AmazonConfigEntry
    api: Incomplete
    previous_devices: set[str]
    def __init__(self, hass: HomeAssistant, entry: AmazonConfigEntry, session: ClientSession) -> None: ...
    async def _async_update_data(self) -> dict[str, AmazonDevice]: ...
    async def _async_remove_device_stale(self, stale_devices: set[str]) -> None: ...
