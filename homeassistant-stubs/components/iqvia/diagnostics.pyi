from .const import CONF_ZIP_CODE as CONF_ZIP_CODE
from .coordinator import IqviaConfigEntry as IqviaConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONF_CITY: str
CONF_DISPLAY_LOCATION: str
CONF_MARKET: str
CONF_TITLE: str
CONF_ZIP_CAP: str
CONF_STATE_CAP: str
TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: IqviaConfigEntry) -> dict[str, Any]: ...
