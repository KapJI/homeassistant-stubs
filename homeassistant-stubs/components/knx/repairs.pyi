from .const import CONF_KNX_KNXKEY_PASSWORD as CONF_KNX_KNXKEY_PASSWORD, DOMAIN as DOMAIN, KNXConfigEntryData as KNXConfigEntryData, REPAIR_ISSUE_DATA_SECURE_GROUP_KEY as REPAIR_ISSUE_DATA_SECURE_GROUP_KEY
from .knx_module import KNXModule as KNXModule
from .storage.keyring import DEFAULT_KNX_KEYRING_FILENAME as DEFAULT_KNX_KEYRING_FILENAME, save_uploaded_knxkeys_file as save_uploaded_knxkeys_file
from .telegrams import SIGNAL_KNX_DATA_SECURE_ISSUE_TELEGRAM as SIGNAL_KNX_DATA_SECURE_ISSUE_TELEGRAM, TelegramDict as TelegramDict
from collections.abc import Callable as Callable
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import RepairsFlow as RepairsFlow
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import selector as selector
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from typing import Any, Final
from xknx.telegram import Telegram as Telegram

CONF_KEYRING_FILE: Final[str]

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
@callback
def data_secure_group_key_issue_dispatcher(knx_module: KNXModule) -> Callable[[], None]: ...
@callback
def _data_secure_group_key_issue_handler(knx_module: KNXModule, telegram: Telegram, telegram_dict: TelegramDict) -> None: ...

class DataSecureGroupIssueRepairFlow(RepairsFlow):
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_secure_knxkeys(self, user_input: dict[str, Any] | None = None) -> data_entry_flow.FlowResult: ...
    @callback
    def finish_flow(self, new_entry_data: KNXConfigEntryData) -> data_entry_flow.FlowResult: ...
