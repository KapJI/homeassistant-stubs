from . import AsusWrtConfigEntry as AsusWrtConfigEntry
from .router import get_device_identifier as get_device_identifier
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data, device_entry_as_dict as device_entry_as_dict, entity_entry_as_dict as entity_entry_as_dict
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, CONF_PASSWORD as CONF_PASSWORD, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete
TO_REDACT_DEV: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: AsusWrtConfigEntry) -> dict[str, dict[str, Any]]: ...
