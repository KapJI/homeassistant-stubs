from .const import CONF_LOGIN_DATA as CONF_LOGIN_DATA, _LOGGER as _LOGGER
from _typeshed import Incomplete
from aioamazondevices.api import AmazonDevice
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

SCAN_INTERVAL: int
type AmazonConfigEntry = ConfigEntry[AmazonDevicesCoordinator]

class AmazonDevicesCoordinator(DataUpdateCoordinator[dict[str, AmazonDevice]]):
    config_entry: AmazonConfigEntry
    api: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AmazonConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, AmazonDevice]: ...
