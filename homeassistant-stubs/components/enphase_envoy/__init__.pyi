from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import EnphaseConfigEntry as EnphaseConfigEntry, EnphaseUpdateCoordinator as EnphaseUpdateCoordinator
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.httpx_client import get_async_client as get_async_client

async def async_setup_entry(hass: HomeAssistant, entry: EnphaseConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: EnphaseConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: EnphaseConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
