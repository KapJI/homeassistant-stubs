from .config_flow import HomeAssistantSkyConnectMultiPanOptionsFlowHandler as HomeAssistantSkyConnectMultiPanOptionsFlowHandler
from _typeshed import Incomplete
from homeassistant.components.homeassistant_hardware.repair_helpers import ISSUE_MULTI_PAN_MIGRATION as ISSUE_MULTI_PAN_MIGRATION, MultiPanMigrationRepairFlow as MultiPanMigrationRepairFlow
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow, RepairsFlowResult as RepairsFlowResult
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any, override

class SkyConnectMultiPanMigrationRepairFlow(MultiPanMigrationRepairFlow, HomeAssistantSkyConnectMultiPanOptionsFlowHandler):
    _repair_config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    @override
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> RepairsFlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
