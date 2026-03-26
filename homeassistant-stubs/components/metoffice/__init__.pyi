from .const import DOMAIN as DOMAIN
from .coordinator import MetOfficeConfigEntry as MetOfficeConfigEntry, MetOfficeRuntimeData as MetOfficeRuntimeData, MetOfficeUpdateCoordinator as MetOfficeUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: MetOfficeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def get_device_info(coordinates: str, name: str) -> DeviceInfo: ...
