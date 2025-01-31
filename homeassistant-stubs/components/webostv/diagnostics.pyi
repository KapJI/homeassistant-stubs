from . import WebOsTvConfigEntry as WebOsTvConfigEntry
from _typeshed import Incomplete
from aiowebostv import WebOsClient as WebOsClient
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_HOST as CONF_HOST, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: WebOsTvConfigEntry) -> dict[str, Any]: ...
