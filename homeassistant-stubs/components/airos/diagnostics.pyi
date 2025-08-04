from .coordinator import AirOSConfigEntry as AirOSConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

IP_REDACT: Incomplete
HW_REDACT: Incomplete
TO_REDACT_HA: Incomplete
TO_REDACT_AIROS: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AirOSConfigEntry) -> dict[str, Any]: ...
