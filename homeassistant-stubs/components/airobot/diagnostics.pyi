from .coordinator import AirobotConfigEntry as AirobotConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT_CONFIG: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AirobotConfigEntry) -> dict[str, Any]: ...
