from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.repairs import RepairsFlow as RepairsFlow
from homeassistant.core import HomeAssistant as HomeAssistant

class MQTTDeviceEntryMigration(RepairsFlow):
    entry_id: Incomplete
    subentry_id: Incomplete
    name: Incomplete
    def __init__(self, entry_id: str, subentry_id: str, name: str) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, str] | None = None) -> data_entry_flow.FlowResult: ...

async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
