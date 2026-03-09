from .const import DOMAIN as DOMAIN
from .coordinator import LitterRobotConfigEntry as LitterRobotConfigEntry, LitterRobotDataUpdateCoordinator as LitterRobotDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: LitterRobotConfigEntry, device_entry: DeviceEntry) -> bool: ...
