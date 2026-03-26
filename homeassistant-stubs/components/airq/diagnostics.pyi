from . import AirQConfigEntry as AirQConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

REDACT_CONFIG: Incomplete
REDACT_DEVICE_INFO: Incomplete
REDACT_COORDINATOR_DATA: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AirQConfigEntry) -> dict[str, Any]: ...
