from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from pyunifiprotect import ProtectApiClient as ProtectApiClient
from pyunifiprotect.data import Bootstrap as Bootstrap, NVR as NVR, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel

_LOGGER: Incomplete

async def async_migrate_data(hass: HomeAssistant, entry: ConfigEntry, protect: ProtectApiClient) -> None: ...
async def async_get_bootstrap(protect: ProtectApiClient) -> Bootstrap: ...
async def async_migrate_buttons(hass: HomeAssistant, entry: ConfigEntry, protect: ProtectApiClient) -> None: ...
async def async_migrate_device_ids(hass: HomeAssistant, entry: ConfigEntry, protect: ProtectApiClient) -> None: ...
