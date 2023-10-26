from . import CONF_CLOUDHOOK_URL as CONF_CLOUDHOOK_URL, WithingsData as WithingsData
from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_WEBHOOK_ID as CONF_WEBHOOK_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
