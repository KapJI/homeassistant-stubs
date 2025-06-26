from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import LaMetricConfigEntry as LaMetricConfigEntry, LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: LaMetricConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LaMetricConfigEntry) -> bool: ...
