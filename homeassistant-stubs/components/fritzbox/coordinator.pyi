from .const import CONF_CONNECTIONS as CONF_CONNECTIONS, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pyfritzhome import Fritzhome as Fritzhome, FritzhomeDevice as FritzhomeDevice
from typing import Any

class FritzboxDataUpdateCoordinator(DataUpdateCoordinator):
    configuration_url: str
    entry: Any
    fritz: Any
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    def _update_fritz_devices(self) -> dict[str, FritzhomeDevice]: ...
    async def _async_update_data(self) -> dict[str, FritzhomeDevice]: ...
