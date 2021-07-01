from . import DOMAIN as DOMAIN
from collections.abc import Iterable
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, SERVICE_ALARM_ARM_AWAY as SERVICE_ALARM_ARM_AWAY, SERVICE_ALARM_ARM_CUSTOM_BYPASS as SERVICE_ALARM_ARM_CUSTOM_BYPASS, SERVICE_ALARM_ARM_HOME as SERVICE_ALARM_ARM_HOME, SERVICE_ALARM_ARM_NIGHT as SERVICE_ALARM_ARM_NIGHT, SERVICE_ALARM_DISARM as SERVICE_ALARM_DISARM, SERVICE_ALARM_TRIGGER as SERVICE_ALARM_TRIGGER, STATE_ALARM_ARMED_AWAY as STATE_ALARM_ARMED_AWAY, STATE_ALARM_ARMED_CUSTOM_BYPASS as STATE_ALARM_ARMED_CUSTOM_BYPASS, STATE_ALARM_ARMED_HOME as STATE_ALARM_ARMED_HOME, STATE_ALARM_ARMED_NIGHT as STATE_ALARM_ARMED_NIGHT, STATE_ALARM_DISARMED as STATE_ALARM_DISARMED, STATE_ALARM_TRIGGERED as STATE_ALARM_TRIGGERED
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, State as State
from typing import Any, Final

_LOGGER: Final[Any]
VALID_STATES: Final[set[str]]

async def _async_reproduce_state(hass: HomeAssistant, state: State, *, context: Union[Context, None] = ..., reproduce_options: Union[dict[str, Any], None] = ...) -> None: ...
async def async_reproduce_states(hass: HomeAssistant, states: Iterable[State], *, context: Union[Context, None] = ..., reproduce_options: Union[dict[str, Any], None] = ...) -> None: ...
