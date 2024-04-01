from .const import DOMAIN as DOMAIN, REG_KEY as REG_KEY
from contextvars import ContextVar
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.integration_platform import async_process_integration_platforms as async_process_integration_platforms
from typing import Protocol

current_domain: ContextVar[str]

async def async_setup(hass: HomeAssistant) -> None: ...

class GroupProtocol(Protocol):
    def async_describe_on_off_states(self, hass: HomeAssistant, registry: GroupIntegrationRegistry) -> None: ...

def _process_group_platform(hass: HomeAssistant, domain: str, platform: GroupProtocol) -> None: ...

class GroupIntegrationRegistry:
    on_off_mapping: dict[str, str]
    off_on_mapping: dict[str, str]
    on_states_by_domain: dict[str, set]
    exclude_domains: set
    def exclude_domain(self) -> None: ...
    def on_off_states(self, on_states: set, off_state: str) -> None: ...
