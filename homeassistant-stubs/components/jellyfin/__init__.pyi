from .client_wrapper import CannotConnect as CannotConnect, InvalidAuth as InvalidAuth, create_client as create_client, validate_input as validate_input
from .const import CONF_CLIENT_DEVICE_ID as CONF_CLIENT_DEVICE_ID, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import JellyfinDataUpdateCoordinator as JellyfinDataUpdateCoordinator, SessionsDataUpdateCoordinator as SessionsDataUpdateCoordinator
from .models import JellyfinData as JellyfinData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
