from homeassistant.components.repairs import RepairsFlow as RepairsFlow, RepairsFlowResult as RepairsFlowResult
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

ISSUE_MULTI_PAN_MIGRATION: str

@callback
def _multi_pan_issue_id(config_entry: ConfigEntry) -> str: ...
@callback
def async_create_multi_pan_migration_issue(hass: HomeAssistant, domain: str, config_entry: ConfigEntry) -> None: ...
@callback
def async_delete_multi_pan_migration_issue(hass: HomeAssistant, domain: str, config_entry: ConfigEntry) -> None: ...

class MultiPanMigrationRepairFlow(RepairsFlow):
    _repair_config_entry: ConfigEntry
    @property
    def config_entry(self) -> ConfigEntry: ...
    async def _async_step_start_migration(self) -> RepairsFlowResult: ...
