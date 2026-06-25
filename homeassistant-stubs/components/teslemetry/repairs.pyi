from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .const import VEHICLE_ISSUE_LEARN_MORE as VEHICLE_ISSUE_LEARN_MORE
from _typeshed import Incomplete
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow, RepairsFlowResult as RepairsFlowResult
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.core import HomeAssistant as HomeAssistant

class VehicleMetadataRepairFlow(RepairsFlow):
    entry: Incomplete
    vin: Incomplete
    issue_type: Incomplete
    placeholders: Incomplete
    def __init__(self, entry: TeslemetryConfigEntry, vin: str, issue_type: str, vehicle: str) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> RepairsFlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
