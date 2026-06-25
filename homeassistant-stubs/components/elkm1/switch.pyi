from . import ElkM1ConfigEntry as ElkM1ConfigEntry
from .const import ATTR_DURATION as ATTR_DURATION, DOMAIN as DOMAIN
from .entity import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from .models import ELKM1Data as ELKM1Data
from _typeshed import Incomplete
from datetime import timedelta
from elkm1_lib.const import ThermostatMode
from elkm1_lib.elements import Element as Element
from elkm1_lib.elk import Elk as Elk
from elkm1_lib.outputs import Output as Output
from elkm1_lib.thermostats import Thermostat as Thermostat
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import service as service
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import VolDictType as VolDictType
from typing import Any, override

SERVICE_SWITCH_OUTPUT_TURN_ON_FOR: str
ELK_OUTPUT_TURN_ON_FOR_SERVICE_SCHEMA: VolDictType

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ElkOutput(ElkAttachedEntity, SwitchEntity):
    _element: Output
    @property
    @override
    def is_on(self) -> bool: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_switch_output_turn_on_for(self, duration: timedelta) -> None: ...

class ElkThermostatEMHeat(ElkEntity, SwitchEntity):
    _element: Thermostat
    _unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, element: Element, elk: Elk, elk_data: ELKM1Data) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    def _elk_set(self, mode: ThermostatMode) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_switch_output_turn_on_for(self, duration: timedelta) -> None: ...
