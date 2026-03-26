from . import DOMAIN as DOMAIN, SERVICE_CLEAN_AREA as SERVICE_CLEAN_AREA, SERVICE_RETURN_TO_BASE as SERVICE_RETURN_TO_BASE, SERVICE_START as SERVICE_START, VacuumEntityFeature as VacuumEntityFeature
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import area_registry as ar, intent as intent

_LOGGER: Incomplete
INTENT_VACUUM_START: str
INTENT_VACUUM_RETURN_TO_BASE: str
INTENT_VACUUM_CLEAN_AREA: str

async def async_setup_intents(hass: HomeAssistant) -> None: ...

class CleanAreaIntentHandler(intent.IntentHandler):
    intent_type = INTENT_VACUUM_CLEAN_AREA
    platforms: Incomplete
    description: str
    @property
    def slot_schema(self) -> dict: ...
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...
    async def _async_handle_service(self, intent_obj: intent.Intent, match_result: intent.MatchTargetsResult, matched_areas: list[ar.AreaEntry]) -> intent.IntentResponse: ...
