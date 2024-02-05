from .const import DOMAIN as DOMAIN, SERVICE_NAME as SERVICE_NAME
from .coordinator import FastdotcomDataUpdateCoordindator as FastdotcomDataUpdateCoordindator
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

def async_setup_services(hass: HomeAssistant) -> None: ...
