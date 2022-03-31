from collections.abc import Callable as Callable
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TITLE as ATTR_TITLE
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_REPEAT as CONF_REPEAT, CONF_STATE as CONF_STATE, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_IDLE as STATE_IDLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers import service as service
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity
from homeassistant.helpers.event import async_track_point_in_time as async_track_point_in_time, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.dt import now as now
from typing import Any

_LOGGER: Any
DOMAIN: str
CONF_CAN_ACK: str
CONF_NOTIFIERS: str
CONF_SKIP_FIRST: str
CONF_ALERT_MESSAGE: str
CONF_DONE_MESSAGE: str
CONF_TITLE: str
CONF_DATA: str
DEFAULT_CAN_ACK: bool
DEFAULT_SKIP_FIRST: bool
ALERT_SCHEMA: Any
CONFIG_SCHEMA: Any
ALERT_SERVICE_SCHEMA: Any

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class Alert(ToggleEntity):
    _attr_should_poll: bool
    hass: Any
    _attr_name: Any
    _alert_state: Any
    _skip_first: Any
    _data: Any
    _message_template: Any
    _done_message_template: Any
    _title_template: Any
    _notifiers: Any
    _can_ack: Any
    _delay: Any
    _next_delay: int
    _firing: bool
    _ack: bool
    _cancel: Any
    _send_done_message: bool
    entity_id: Any
    def __init__(self, hass: HomeAssistant, entity_id: str, name: str, watched_entity_id: str, state: str, repeat: list[float], skip_first: bool, message_template: Union[Template, None], done_message_template: Union[Template, None], notifiers: list[str], can_ack: bool, title_template: Union[Template, None], data: dict[Any, Any]) -> None: ...
    @property
    def state(self) -> str: ...
    async def watched_entity_change(self, event: Event) -> None: ...
    async def begin_alerting(self) -> None: ...
    async def end_alerting(self) -> None: ...
    async def _schedule_notify(self) -> None: ...
    async def _notify(self, *args: Any) -> None: ...
    async def _notify_done_message(self) -> None: ...
    async def _send_notification_message(self, message: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_toggle(self, **kwargs: Any) -> None: ...
