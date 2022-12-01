from .const import DOMAIN as DOMAIN
from .issue_handler import ConfirmRepairFlow as ConfirmRepairFlow, RepairsFlowManager as RepairsFlowManager
from .models import RepairsFlow as RepairsFlow
from homeassistant.core import HomeAssistant

def repairs_flow_manager(hass: HomeAssistant) -> Union[RepairsFlowManager, None]: ...
