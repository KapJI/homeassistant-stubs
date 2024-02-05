from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.components import webhook as webhook
from homeassistant.const import CONF_WEBHOOK_ID as CONF_WEBHOOK_ID
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.network import get_url as get_url
from typing import Any

class EcowittConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _webhook_id: str
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...

class InvalidPort(HomeAssistantError): ...
