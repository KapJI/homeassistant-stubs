from . import PyNUTData as PyNUTData
from .const import DOMAIN as DOMAIN, PYNUT_DATA as PYNUT_DATA, PYNUT_UNIQUE_ID as PYNUT_UNIQUE_ID
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, dict[str, Any]]: ...
