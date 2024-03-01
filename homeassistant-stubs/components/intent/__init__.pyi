from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiohttp import web as web
from homeassistant.components import http as http
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, SERVICE_CLOSE_COVER as SERVICE_CLOSE_COVER, SERVICE_OPEN_COVER as SERVICE_OPEN_COVER, SERVICE_SET_COVER_POSITION as SERVICE_SET_COVER_POSITION
from homeassistant.components.http.data_validator import RequestDataValidator as RequestDataValidator
from homeassistant.components.lock import SERVICE_LOCK as SERVICE_LOCK, SERVICE_UNLOCK as SERVICE_UNLOCK
from homeassistant.components.valve import SERVICE_CLOSE_VALVE as SERVICE_CLOSE_VALVE, SERVICE_OPEN_VALVE as SERVICE_OPEN_VALVE, SERVICE_SET_VALVE_POSITION as SERVICE_SET_VALVE_POSITION
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers import integration_platform as integration_platform, intent as intent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Protocol

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class IntentPlatformProtocol(Protocol):
    async def async_setup_intents(self, hass: HomeAssistant) -> None: ...

class OnOffIntentHandler(intent.ServiceIntentHandler):
    async def async_call_service(self, domain: str, service: str, intent_obj: intent.Intent, state: State) -> None: ...

class GetStateIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    slot_schema: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class NevermindIntentHandler(intent.IntentHandler):
    intent_type: Incomplete
    async def async_handle(self, intent_obj: intent.Intent) -> intent.IntentResponse: ...

class SetPositionIntentHandler(intent.DynamicServiceIntentHandler):
    def __init__(self) -> None: ...
    def get_domain_and_service(self, intent_obj: intent.Intent, state: State) -> tuple[str, str]: ...

async def _async_process_intent(hass: HomeAssistant, domain: str, platform: IntentPlatformProtocol) -> None: ...

class IntentHandleView(http.HomeAssistantView):
    url: str
    name: str
    async def post(self, request: web.Request, data: dict[str, Any]) -> web.Response: ...
