from .const import CONF_ALERT_MESSAGE as CONF_ALERT_MESSAGE, CONF_CAN_ACK as CONF_CAN_ACK, CONF_DATA as CONF_DATA, CONF_DONE_MESSAGE as CONF_DONE_MESSAGE, CONF_NOTIFIERS as CONF_NOTIFIERS, CONF_SKIP_FIRST as CONF_SKIP_FIRST, CONF_TITLE as CONF_TITLE, DEFAULT_CAN_ACK as DEFAULT_CAN_ACK, DEFAULT_SKIP_FIRST as DEFAULT_SKIP_FIRST, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TITLE as ATTR_TITLE
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_REPEAT as CONF_REPEAT, CONF_STATE as CONF_STATE, SERVICE_TOGGLE as SERVICE_TOGGLE, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_IDLE as STATE_IDLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.event import async_track_point_in_time as async_track_point_in_time, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.dt import now as now
from typing import Any

ALERT_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class Alert(Entity):
    _attr_should_poll: bool
    hass: Incomplete
    _attr_name: Incomplete
    _alert_state: Incomplete
    _skip_first: Incomplete
    _data: Incomplete
    _message_template: Incomplete
    _done_message_template: Incomplete
    _title_template: Incomplete
    _notifiers: Incomplete
    _can_ack: Incomplete
    _delay: Incomplete
    _next_delay: int
    _firing: bool
    _ack: bool
    _cancel: Incomplete
    _send_done_message: bool
    entity_id: Incomplete
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
