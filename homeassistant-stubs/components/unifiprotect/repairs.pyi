from .const import CONF_ALLOW_EA as CONF_ALLOW_EA, DOMAIN as DOMAIN
from .utils import async_create_api_client as async_create_api_client
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.automation import EVENT_AUTOMATION_RELOADED as EVENT_AUTOMATION_RELOADED, automations_with_entity as automations_with_entity
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity
from pyunifiprotect import ProtectApiClient as ProtectApiClient
from typing import Any

_LOGGER: Incomplete

async def async_create_repairs(hass: HomeAssistant, entry: ConfigEntry, protect: ProtectApiClient) -> None: ...
async def _deprecate_smart_sensor(hass: HomeAssistant, entry: ConfigEntry, protect: ProtectApiClient, *args: Any, **kwargs: Any) -> None: ...

class EAConfirm(RepairsFlow):
    _api: ProtectApiClient
    _entry: ConfigEntry
    def __init__(self, api: ProtectApiClient, entry: ConfigEntry) -> None: ...
    def _async_get_placeholders(self) -> Union[dict[str, str], None]: ...
    async def async_step_init(self, user_input: Union[dict[str, str], None] = ...) -> data_entry_flow.FlowResult: ...
    async def async_step_start(self, user_input: Union[dict[str, str], None] = ...) -> data_entry_flow.FlowResult: ...
    async def async_step_confirm(self, user_input: Union[dict[str, str], None] = ...) -> data_entry_flow.FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: Union[dict[str, Union[str, int, float, None]], None]) -> RepairsFlow: ...
