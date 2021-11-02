from .const import DOMAIN as DOMAIN, FRITZ_SERVICES as FRITZ_SERVICES, SERVICE_REBOOT as SERVICE_REBOOT, SERVICE_RECONNECT as SERVICE_RECONNECT
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.service import async_extract_config_entry_ids as async_extract_config_entry_ids
from typing import Any

_LOGGER: Any

async def async_setup_services(hass: HomeAssistant) -> None: ...
async def _async_get_configured_fritz_tools(hass: HomeAssistant, service_call: ServiceCall) -> list: ...
async def async_unload_services(hass: HomeAssistant) -> None: ...
