from .const import DOMAIN as DOMAIN
from .models import ELKM1Data as ELKM1Data
from _typeshed import Incomplete
from elkm1_lib.elk import Elk as Elk, Panel as Panel
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

SPEAK_SERVICE_SCHEMA: Incomplete
SET_TIME_SERVICE_SCHEMA: Incomplete

def _find_elk_by_prefix(hass: HomeAssistant, prefix: str) -> Elk | None: ...
@callback
def _async_get_elk_panel(service: ServiceCall) -> Panel: ...
@callback
def _speak_word_service(service: ServiceCall) -> None: ...
@callback
def _speak_phrase_service(service: ServiceCall) -> None: ...
@callback
def _set_time_service(service: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
