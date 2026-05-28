from .config_flow import HomeAssistantYellowMultiPanOptionsFlowHandler as HomeAssistantYellowMultiPanOptionsFlowHandler
from _typeshed import Incomplete
from homeassistant.components.homeassistant_hardware.repair_helpers import ISSUE_MULTI_PAN_MIGRATION as ISSUE_MULTI_PAN_MIGRATION, MultiPanMigrationRepairFlow as MultiPanMigrationRepairFlow
from homeassistant.components.repairs import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlow as RepairsFlow, RepairsFlowResult as RepairsFlowResult
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant

class YellowMultiPanMigrationRepairFlow(MultiPanMigrationRepairFlow, HomeAssistantYellowMultiPanOptionsFlowHandler):
    _repair_config_entry: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def async_step_main_menu(self, _: None = None) -> RepairsFlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
