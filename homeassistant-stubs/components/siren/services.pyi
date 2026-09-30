from . import SirenEntity as SirenEntity
from .const import ATTR_DURATION as ATTR_DURATION, ATTR_TONE as ATTR_TONE, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL, DATA_COMPONENT as DATA_COMPONENT, SirenEntityFeature as SirenEntityFeature
from homeassistant.const import SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import TypedDict

TURN_ON_SCHEMA: VolDictType

class SirenTurnOnServiceParameters(TypedDict, total=False):
    tone: int | str
    duration: int
    volume_level: float

def process_turn_on_params(siren: SirenEntity, params: SirenTurnOnServiceParameters) -> SirenTurnOnServiceParameters: ...
async def _async_handle_turn_on_service(siren: SirenEntity, call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
