import aiopulse
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_ID as CONF_ID
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class AcmedaFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    discovered_hubs: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_create(self, hub: aiopulse.Hub) -> FlowResult: ...
