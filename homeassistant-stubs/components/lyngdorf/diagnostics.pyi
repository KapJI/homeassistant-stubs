from .const import CONF_SERIAL_NUMBER as CONF_SERIAL_NUMBER, SSDP_ST as SSDP_ST
from .models import LyngdorfConfigEntry as LyngdorfConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.components.ssdp import async_get_discovery_info_by_st as async_get_discovery_info_by_st
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.service_info.ssdp import ATTR_UPNP_SERIAL as ATTR_UPNP_SERIAL
from typing import Any

_TRIMS: Incomplete
TO_REDACT: Incomplete

async def _async_ssdp_description(hass: HomeAssistant, serial: str) -> dict[str, Any] | None: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: LyngdorfConfigEntry) -> dict[str, Any]: ...
