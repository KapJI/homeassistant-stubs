from .const import DOMAIN as DOMAIN
from .coordinator import LitterRobotConfigEntry as LitterRobotConfigEntry, LitterRobotDataUpdateCoordinator as LitterRobotDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import AnyDeviceEntry as AnyDeviceEntry
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LitterRobotConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: LitterRobotConfigEntry, device_entry: AnyDeviceEntry) -> bool: ...
