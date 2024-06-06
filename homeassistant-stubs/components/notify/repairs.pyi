from .const import DOMAIN as DOMAIN
from homeassistant.components.repairs import RepairsFlow as RepairsFlow
from homeassistant.components.repairs.issue_handler import ConfirmRepairFlow as ConfirmRepairFlow
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def migrate_notify_issue(hass: HomeAssistant, domain: str, integration_title: str, breaks_in_ha_version: str, service_name: str | None = None) -> None: ...
async def async_create_fix_flow(hass: HomeAssistant, issue_id: str, data: dict[str, str | int | float | None] | None) -> RepairsFlow: ...
