from .const import ATTR_APPLICATION as ATTR_APPLICATION, ATTR_URL as ATTR_URL, DOMAIN as DOMAIN, LOGGER as LOGGER, SERVICE_LOAD_URL as SERVICE_LOAD_URL, SERVICE_START_APPLICATION as SERVICE_START_APPLICATION
from collections.abc import Callable as Callable
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall

async def async_setup_services(hass: HomeAssistant) -> None: ...
