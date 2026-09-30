from .const import CONF_GROUP as CONF_GROUP, CONF_LABEL as CONF_LABEL, CONF_MAC_ADDRESS as CONF_MAC_ADDRESS, CONF_NETWORK_NAME as CONF_NETWORK_NAME, CONF_SERIAL as CONF_SERIAL, CONF_TITLE as CONF_TITLE
from .coordinator import LIFXConfigEntry as LIFXConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_LOCATION as CONF_LOCATION
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: LIFXConfigEntry) -> dict[str, Any]: ...
