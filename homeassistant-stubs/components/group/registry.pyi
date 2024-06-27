from .const import DOMAIN as DOMAIN, REG_KEY as REG_KEY
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.climate import HVACMode as HVACMode
from homeassistant.components.vacuum import STATE_CLEANING as STATE_CLEANING, STATE_ERROR as STATE_ERROR, STATE_RETURNING as STATE_RETURNING
from homeassistant.components.water_heater import STATE_ECO as STATE_ECO, STATE_ELECTRIC as STATE_ELECTRIC, STATE_GAS as STATE_GAS, STATE_HEAT_PUMP as STATE_HEAT_PUMP, STATE_HIGH_DEMAND as STATE_HIGH_DEMAND, STATE_PERFORMANCE as STATE_PERFORMANCE
from homeassistant.const import Platform as Platform, STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_CUSTOM_BYPASS as STATE_ALARM_ARMED_CUSTOM_BYPASS, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_ARMED_VACATION as STATE_ALARM_ARMED_VACATION, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED, STATE_CLOSED as STATE_CLOSED, STATE_HOME as STATE_HOME, STATE_IDLE as STATE_IDLE, STATE_LOCKED as STATE_LOCKED, STATE_LOCKING as STATE_LOCKING, STATE_NOT_HOME as STATE_NOT_HOME, STATE_OFF as STATE_OFF, STATE_OK as STATE_OK, STATE_ON as STATE_ON, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING, STATE_PAUSED as STATE_PAUSED, STATE_PLAYING as STATE_PLAYING, STATE_PROBLEM as STATE_PROBLEM, STATE_UNLOCKED as STATE_UNLOCKED, STATE_UNLOCKING as STATE_UNLOCKING
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.integration_platform import async_process_integration_platforms as async_process_integration_platforms
from typing import Protocol

EXCLUDED_DOMAINS: set[Platform | str]
ON_OFF_STATES: dict[Platform | str, tuple[set[str], str, str]]

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
    def on_off_states(self, domain: Platform | str, on_states: set[str], default_on_state: str, off_state: str) -> None: ...
