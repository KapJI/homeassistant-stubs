from .config_flow import async_request_token as async_request_token
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import RepairsFlow as RepairsFlow
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResult as FlowResult

class MigrateToV2ApiRepairFlow(RepairsFlow):
    entry: Incomplete
    def __init__(self, entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> FlowResult: ...
    async def async_step_authorize(self, user_input: dict[str, str] | None = None) -> FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
