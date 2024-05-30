from .const import DOMAIN as DOMAIN, SERVICE_PHASES as SERVICE_PHASES, SERVICE_SETTINGS as SERVICE_SETTINGS, SERVICE_SMARTMETER as SERVICE_SMARTMETER, SERVICE_WATERMETER as SERVICE_WATERMETER
from .coordinator import P1MonitorDataUpdateCoordinator as P1MonitorDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
