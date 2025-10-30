from .const import CONF_VIN as CONF_VIN
from .coordinator import VolvoConfigEntry as VolvoConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_API_KEY as CONF_API_KEY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.redact import async_redact_data as async_redact_data
from typing import Any

_TO_REDACT_ENTRY: Incomplete
_TO_REDACT_DATA: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: VolvoConfigEntry) -> dict[str, Any]: ...
