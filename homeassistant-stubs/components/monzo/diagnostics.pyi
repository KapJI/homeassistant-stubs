from .const import CONF_CLOUDHOOK_URL as CONF_CLOUDHOOK_URL, CONF_WEBHOOK_URL as CONF_WEBHOOK_URL, NON_TRANSFER_ACCOUNT_TYPES as NON_TRANSFER_ACCOUNT_TYPES
from .coordinator import MonzoConfigEntry as MonzoConfigEntry
from _typeshed import Incomplete
from homeassistant.components.diagnostics import async_redact_data as async_redact_data
from homeassistant.const import CONF_TOKEN as CONF_TOKEN, CONF_WEBHOOK_ID as CONF_WEBHOOK_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

def _account_diagnostics(account: dict[str, Any]) -> dict[str, Any]: ...
def _pot_diagnostics(pot: dict[str, Any], account_ids: set[str]) -> dict[str, Any]: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: MonzoConfigEntry) -> dict[str, Any]: ...
