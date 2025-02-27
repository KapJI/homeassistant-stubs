from . import services as services
from .const import DOMAIN as DOMAIN
from .coordinator import HeosConfigEntry as HeosConfigEntry, HeosCoordinator as HeosCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: Incomplete
MIN_UPDATE_SOURCES: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: HeosConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HeosConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: HeosConfigEntry, device: dr.DeviceEntry) -> bool: ...
