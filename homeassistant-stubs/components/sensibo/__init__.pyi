from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, PLATFORMS as PLATFORMS
from .coordinator import SensiboDataUpdateCoordinator as SensiboDataUpdateCoordinator
from .util import NoDevicesError as NoDevicesError, NoUsernameError as NoUsernameError, async_validate_api as async_validate_api
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry

async def async_setup_entry(hass: HomeAssistant, entry: SensiboConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: ConfigEntry, device: DeviceEntry) -> bool: ...
