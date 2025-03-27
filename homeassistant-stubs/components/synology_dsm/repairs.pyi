from .const import CONF_BACKUP_PATH as CONF_BACKUP_PATH, CONF_BACKUP_SHARE as CONF_BACKUP_SHARE, DOMAIN as DOMAIN, ISSUE_MISSING_BACKUP_SETUP as ISSUE_MISSING_BACKUP_SETUP, SYNOLOGY_CONNECTION_EXCEPTIONS as SYNOLOGY_CONNECTION_EXCEPTIONS
from .coordinator import SynologyDSMConfigEntry as SynologyDSMConfigEntry
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from synology_dsm.api.file_station.models import SynoFileSharedFolder as SynoFileSharedFolder

LOGGER: Incomplete

class MissingBackupSetupRepairFlow(RepairsFlow):
    entry: Incomplete
    issue_id: Incomplete
    def __init__(self, entry: SynologyDSMConfigEntry, issue_id: str) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_ignore(self, _: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
