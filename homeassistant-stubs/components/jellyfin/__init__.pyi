from .client_wrapper import CannotConnect as CannotConnect, InvalidAuth as InvalidAuth, create_client as create_client, validate_input as validate_input
from .const import CONF_CLIENT_DEVICE_ID as CONF_CLIENT_DEVICE_ID, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import JellyfinConfigEntry as JellyfinConfigEntry, JellyfinDataUpdateCoordinator as JellyfinDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: JellyfinConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: JellyfinConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: JellyfinConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
