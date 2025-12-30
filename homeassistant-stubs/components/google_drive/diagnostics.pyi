from .const import DOMAIN as DOMAIN
from .coordinator import GoogleDriveConfigEntry as GoogleDriveConfigEntry
from _typeshed import Incomplete
from homeassistant.components.backup import BackupManager as BackupManager
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: GoogleDriveConfigEntry) -> dict[str, Any]: ...
