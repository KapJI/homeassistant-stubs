from . import BesenConfigEntry as BesenConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_NAME as CONF_NAME, CONF_PIN as CONF_PIN
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_DEVICE_NAME: str
CONF_SERIAL: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: BesenConfigEntry) -> dict[str, Any]: ...
