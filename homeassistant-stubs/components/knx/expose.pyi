from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, KNX_ADDRESS as KNX_ADDRESS
from .schema import ExposeSchema as ExposeSchema
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from xknx import XKNX as XKNX

_LOGGER: Incomplete

def create_knx_exposure(hass: HomeAssistant, xknx: XKNX, config: ConfigType) -> KNXExposeSensor | KNXExposeTime: ...

class KNXExposeSensor:
    hass: Incomplete
    xknx: Incomplete
    entity_id: Incomplete
    expose_attribute: Incomplete
    expose_default: Incomplete
    expose_type: Incomplete
    value_template: Incomplete
    _remove_listener: Incomplete
    device: Incomplete
    def __init__(self, hass: HomeAssistant, xknx: XKNX, config: ConfigType) -> None: ...
    def async_register(self) -> None: ...
    def _init_expose_state(self) -> None: ...
    def async_remove(self) -> None: ...
    def _get_expose_value(self, state: State | None) -> bool | int | float | str | None: ...
    async def _async_entity_changed(self, event: Event[EventStateChangedData]) -> None: ...
    async def _async_set_knx_value(self, value: StateType) -> None: ...

class KNXExposeTime:
    xknx: Incomplete
    device: Incomplete
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    def async_register(self) -> None: ...
    def async_remove(self) -> None: ...
