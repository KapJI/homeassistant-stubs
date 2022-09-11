from _typeshed import Incomplete
from collections.abc import Coroutine
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.async_ import gather_with_concurrency as gather_with_concurrency
from typing import Any

FLOW_INIT_LIMIT: int
DISCOVERY_FLOW_DISPATCHER: str

def async_create_flow(hass: HomeAssistant, domain: str, context: dict[str, Any], data: Any) -> None: ...
def _async_init_flow(hass: HomeAssistant, domain: str, context: dict[str, Any], data: Any) -> Union[Coroutine[None, None, FlowResult], None]: ...

class FlowDispatcher:
    hass: Incomplete
    pending_flows: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_setup(self) -> None: ...
    async def _async_start(self, event: Event) -> None: ...
    def async_create(self, domain: str, context: dict[str, Any], data: Any) -> None: ...
