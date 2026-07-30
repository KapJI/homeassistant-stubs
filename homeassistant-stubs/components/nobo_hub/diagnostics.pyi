from . import NoboHubConfigEntry as NoboHubConfigEntry
from .const import ATTR_SERIAL as ATTR_SERIAL, CONF_SERIAL as CONF_SERIAL
from _typeshed import Incomplete
from homeassistant.components.diagnostics import REDACTED as REDACTED, async_redact_data as async_redact_data
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_MAC as CONF_MAC
from homeassistant.core import HomeAssistant as HomeAssistant
from pynobo import ComponentInfo as ComponentInfo
from typing import Any

TO_REDACT_ENTRY: Incomplete
TO_REDACT_HUB: Incomplete
_MODEL_FIELDS: Incomplete

def _component_to_dict(component: ComponentInfo) -> dict[str, Any]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: NoboHubConfigEntry) -> dict[str, Any]: ...
