from .const import CONF_DEVICE_DETAILS as CONF_DEVICE_DETAILS, DEVICE_TYPE as DEVICE_TYPE, DEVICE_URL as DEVICE_URL, _LOGGER as _LOGGER
from .coordinator import VodafoneConfigEntry as VodafoneConfigEntry, VodafoneStationRouter as VodafoneStationRouter
from .utils import async_client_session as async_client_session
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: VodafoneConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: VodafoneConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VodafoneConfigEntry) -> bool: ...
