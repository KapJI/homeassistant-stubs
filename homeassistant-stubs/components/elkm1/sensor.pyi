from . import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from .const import ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN, ELK_USER_CODE_SERVICE_SCHEMA as ELK_USER_CODE_SERVICE_SCHEMA
from _typeshed import Incomplete
from elkm1_lib.counters import Counter as Counter
from elkm1_lib.elements import Element as Element
from elkm1_lib.elk import Elk as Elk
from elkm1_lib.keypads import Keypad as Keypad
from elkm1_lib.panel import Panel as Panel
from elkm1_lib.settings import Setting as Setting
from elkm1_lib.zones import Zone as Zone
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfElectricPotential as UnitOfElectricPotential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SERVICE_SENSOR_COUNTER_REFRESH: str
SERVICE_SENSOR_COUNTER_SET: str
SERVICE_SENSOR_ZONE_BYPASS: str
SERVICE_SENSOR_ZONE_TRIGGER: str
UNDEFINED_TEMPERATURE: int
ELK_SET_COUNTER_SERVICE_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def temperature_to_state(temperature: int, undefined_temperature: int) -> Union[str, None]: ...

class ElkSensor(ElkAttachedEntity, SensorEntity):
    _state: Incomplete
    def __init__(self, element: Element, elk: Elk, elk_data: dict[str, Any]) -> None: ...
    @property
    def native_value(self) -> Union[str, None]: ...
    async def async_counter_refresh(self) -> None: ...
    async def async_counter_set(self, value: Union[int, None] = ...) -> None: ...
    async def async_zone_bypass(self, code: Union[int, None] = ...) -> None: ...
    async def async_zone_trigger(self) -> None: ...

class ElkCounter(ElkSensor):
    _element: Counter
    @property
    def icon(self) -> str: ...
    _state: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...

class ElkKeypad(ElkSensor):
    _element: Keypad
    @property
    def temperature_unit(self) -> str: ...
    @property
    def native_unit_of_measurement(self) -> str: ...
    @property
    def icon(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    _state: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...

class ElkPanel(ElkSensor):
    _attr_entity_category: Incomplete
    _element: Panel
    @property
    def icon(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    _state: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...

class ElkSetting(ElkSensor):
    _element: Setting
    @property
    def icon(self) -> str: ...
    _state: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...

class ElkZone(ElkSensor):
    _element: Zone
    @property
    def icon(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def temperature_unit(self) -> Union[str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    _state: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...
