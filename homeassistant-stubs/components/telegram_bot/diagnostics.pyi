from . import TelegramBotConfigEntry as TelegramBotConfigEntry
from .const import CONF_CHAT_ID as CONF_CHAT_ID
from _typeshed import Incomplete
from homeassistant.components.diagnostics import REDACTED as REDACTED, async_redact_data as async_redact_data
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

TO_REDACT: Incomplete

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: TelegramBotConfigEntry) -> dict[str, Any]: ...
