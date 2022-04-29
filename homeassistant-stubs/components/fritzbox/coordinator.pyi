from .const import CONF_CONNECTIONS as CONF_CONNECTIONS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyfritzhome import Fritzhome as Fritzhome, FritzhomeDevice as FritzhomeDevice

class FritzboxDataUpdateCoordinator(DataUpdateCoordinator):
    configuration_url: str
    entry: Incomplete
    fritz: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    def _update_fritz_devices(self) -> dict[str, FritzhomeDevice]: ...
    async def _async_update_data(self) -> dict[str, FritzhomeDevice]: ...
