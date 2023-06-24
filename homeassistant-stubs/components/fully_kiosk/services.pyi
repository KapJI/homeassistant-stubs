from .const import ATTR_APPLICATION as ATTR_APPLICATION, ATTR_URL as ATTR_URL, DOMAIN as DOMAIN, SERVICE_LOAD_URL as SERVICE_LOAD_URL, SERVICE_START_APPLICATION as SERVICE_START_APPLICATION
from .coordinator import FullyKioskDataUpdateCoordinator as FullyKioskDataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

async def async_setup_services(hass: HomeAssistant) -> None: ...
