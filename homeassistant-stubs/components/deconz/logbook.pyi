from .const import CONF_GESTURE as CONF_GESTURE, DOMAIN as DOMAIN
from .deconz_event import CONF_DECONZ_ALARM_EVENT as CONF_DECONZ_ALARM_EVENT, CONF_DECONZ_EVENT as CONF_DECONZ_EVENT
from .device_trigger import CONF_BOTH_BUTTONS as CONF_BOTH_BUTTONS, CONF_BOTTOM_BUTTONS as CONF_BOTTOM_BUTTONS, CONF_BUTTON_1 as CONF_BUTTON_1, CONF_BUTTON_2 as CONF_BUTTON_2, CONF_BUTTON_3 as CONF_BUTTON_3, CONF_BUTTON_4 as CONF_BUTTON_4, CONF_BUTTON_5 as CONF_BUTTON_5, CONF_BUTTON_6 as CONF_BUTTON_6, CONF_BUTTON_7 as CONF_BUTTON_7, CONF_BUTTON_8 as CONF_BUTTON_8, CONF_CLOSE as CONF_CLOSE, CONF_DIM_DOWN as CONF_DIM_DOWN, CONF_DIM_UP as CONF_DIM_UP, CONF_DOUBLE_PRESS as CONF_DOUBLE_PRESS, CONF_DOUBLE_TAP as CONF_DOUBLE_TAP, CONF_LEFT as CONF_LEFT, CONF_LONG_PRESS as CONF_LONG_PRESS, CONF_LONG_RELEASE as CONF_LONG_RELEASE, CONF_MOVE as CONF_MOVE, CONF_OPEN as CONF_OPEN, CONF_QUADRUPLE_PRESS as CONF_QUADRUPLE_PRESS, CONF_QUINTUPLE_PRESS as CONF_QUINTUPLE_PRESS, CONF_RIGHT as CONF_RIGHT, CONF_ROTATED as CONF_ROTATED, CONF_ROTATED_FAST as CONF_ROTATED_FAST, CONF_ROTATE_FROM_SIDE_1 as CONF_ROTATE_FROM_SIDE_1, CONF_ROTATE_FROM_SIDE_2 as CONF_ROTATE_FROM_SIDE_2, CONF_ROTATE_FROM_SIDE_3 as CONF_ROTATE_FROM_SIDE_3, CONF_ROTATE_FROM_SIDE_4 as CONF_ROTATE_FROM_SIDE_4, CONF_ROTATE_FROM_SIDE_5 as CONF_ROTATE_FROM_SIDE_5, CONF_ROTATE_FROM_SIDE_6 as CONF_ROTATE_FROM_SIDE_6, CONF_ROTATION_STOPPED as CONF_ROTATION_STOPPED, CONF_SHAKE as CONF_SHAKE, CONF_SHORT_PRESS as CONF_SHORT_PRESS, CONF_SHORT_RELEASE as CONF_SHORT_RELEASE, CONF_SIDE_1 as CONF_SIDE_1, CONF_SIDE_2 as CONF_SIDE_2, CONF_SIDE_3 as CONF_SIDE_3, CONF_SIDE_4 as CONF_SIDE_4, CONF_SIDE_5 as CONF_SIDE_5, CONF_SIDE_6 as CONF_SIDE_6, CONF_TOP_BUTTONS as CONF_TOP_BUTTONS, CONF_TRIPLE_PRESS as CONF_TRIPLE_PRESS, CONF_TURN_OFF as CONF_TURN_OFF, CONF_TURN_ON as CONF_TURN_ON, REMOTES as REMOTES, _get_deconz_event_from_device as _get_deconz_event_from_device
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.logbook import LOGBOOK_ENTRY_MESSAGE as LOGBOOK_ENTRY_MESSAGE, LOGBOOK_ENTRY_NAME as LOGBOOK_ENTRY_NAME
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_EVENT as CONF_EVENT, CONF_ID as CONF_ID
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback

ACTIONS: Incomplete
INTERFACES: Incomplete

def _get_device_event_description(modelid: str, event: int) -> tuple[str | None, str | None]: ...
@callback
def async_describe_events(hass: HomeAssistant, async_describe_event: Callable[[str, str, Callable[[Event], dict[str, str]]], None]) -> None: ...
