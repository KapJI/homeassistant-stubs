from . import BoschAlarmConfigEntry as BoschAlarmConfigEntry
from .const import CONF_INSTALLER_CODE as CONF_INSTALLER_CODE, CONF_USER_CODE as CONF_USER_CODE
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: BoschAlarmConfigEntry) -> dict[str, Any]: ...
