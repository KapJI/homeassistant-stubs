from .const import DOMAIN as DOMAIN, REG_KEY as REG_KEY
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.integration_platform import async_process_integration_platforms as async_process_integration_platforms
from typing import Protocol

async def async_setup(hass: HomeAssistant) -> None: ...

class GroupProtocol(Protocol):
    def async_describe_on_off_states(self, hass: HomeAssistant, registry: GroupIntegrationRegistry) -> None: ...

def _process_group_platform(hass: HomeAssistant, domain: str, platform: GroupProtocol) -> None: ...

@dataclass(frozen=True, slots=True)
class SingleStateType:
    on_state: str
    off_state: str
    def __init__(self, on_state, off_state) -> None: ...

class GroupIntegrationRegistry:
    hass: Incomplete
    on_off_mapping: Incomplete
    off_on_mapping: Incomplete
    on_states_by_domain: Incomplete
    exclude_domains: Incomplete
    state_group_mapping: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def exclude_domain(self, domain: str) -> None: ...
    def on_off_states(self, domain: str, on_states: set[str], default_on_state: str, off_state: str) -> None: ...
