from .coordinator import ShellyConfigEntry as ShellyConfigEntry
from .utils import get_rpc_ws_url as get_rpc_ws_url
from _typeshed import Incomplete
from homeassistant.components.bluetooth import async_scanner_by_source as async_scanner_by_source
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ShellyConfigEntry) -> dict[str, Any]: ...
