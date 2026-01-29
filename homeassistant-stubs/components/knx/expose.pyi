from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, KNX_ADDRESS as KNX_ADDRESS
from .schema import ExposeSchema as ExposeSchema
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from dataclasses import dataclass
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import ExposeSensor
from xknx.dpt import DPTBase
from xknx.telegram.address import GroupAddress as GroupAddress, InternalGroupAddress as InternalGroupAddress

_LOGGER: Incomplete

@callback
def create_knx_exposure(hass: HomeAssistant, xknx: XKNX, config: ConfigType) -> KnxExposeEntity | KnxExposeTime: ...
@callback
def create_combined_knx_exposure(hass: HomeAssistant, xknx: XKNX, configs: list[ConfigType]) -> list[KnxExposeEntity | KnxExposeTime]: ...

@dataclass(slots=True)
class KnxExposeOptions:
    attribute: str | None
    group_address: GroupAddress | InternalGroupAddress
    dpt: type[DPTBase]
    respond_to_read: bool
    cooldown: float
    default: Any | None
    value_template: Template | None

def _yaml_config_to_expose_options(config: ConfigType) -> KnxExposeOptions: ...

class KnxExposeEntity:
    hass: Incomplete
    xknx: Incomplete
    entity_id: Incomplete
    _remove_listener: Callable[[], None] | None
    _exposures: Incomplete
    def __init__(self, hass: HomeAssistant, xknx: XKNX, entity_id: str, options: Iterable[KnxExposeOptions]) -> None: ...
    @property
    def name(self) -> str: ...
    @callback
    def async_register(self) -> None: ...
    @callback
    def _init_expose_state(self) -> None: ...
    @callback
    def async_remove(self) -> None: ...
    def _get_expose_value(self, state: State | None, option: KnxExposeOptions) -> bool | int | float | str | None: ...
    async def _async_entity_changed(self, event: Event[EventStateChangedData]) -> None: ...
    async def _async_set_knx_value(self, xknx_expose: ExposeSensor, value: StateType) -> None: ...

class KnxExposeTime:
    xknx: Incomplete
    device: Incomplete
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    @property
    def name(self) -> str: ...
    @callback
    def async_register(self) -> None: ...
    @callback
    def async_remove(self) -> None: ...
