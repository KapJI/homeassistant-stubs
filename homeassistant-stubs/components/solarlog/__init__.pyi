from .const import CONF_HAS_PWD as CONF_HAS_PWD
from .coordinator import SolarLogBasicDataCoordinator as SolarLogBasicDataCoordinator, SolarLogDeviceDataCoordinator as SolarLogDeviceDataCoordinator, SolarLogLongtimeDataCoordinator as SolarLogLongtimeDataCoordinator, SolarlogConfigEntry as SolarlogConfigEntry
from .models import SolarlogIntegrationData as SolarlogIntegrationData
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_TIMEOUT as CONF_TIMEOUT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SolarlogConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SolarlogConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: SolarlogConfigEntry) -> bool: ...
