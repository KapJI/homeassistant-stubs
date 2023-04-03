from .const import CONF_ALLOW_EA as CONF_ALLOW_EA
from .utils import async_create_api_client as async_create_api_client
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from pyunifiprotect import ProtectApiClient as ProtectApiClient

_LOGGER: Incomplete

class EAConfirm(RepairsFlow):
    _api: ProtectApiClient
    _entry: ConfigEntry
    def __init__(self, api: ProtectApiClient, entry: ConfigEntry) -> None: ...
    def _async_get_placeholders(self) -> dict[str, str] | None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = ...) -> data_entry_flow.FlowResult: ...
    async def async_step_start(self, user_input: dict[str, str] | None = ...) -> data_entry_flow.FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = ...) -> data_entry_flow.FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
