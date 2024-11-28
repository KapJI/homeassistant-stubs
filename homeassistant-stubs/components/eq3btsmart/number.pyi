from . import Eq3ConfigEntry as Eq3ConfigEntry
from .const import ENTITY_KEY_COMFORT as ENTITY_KEY_COMFORT, ENTITY_KEY_ECO as ENTITY_KEY_ECO, ENTITY_KEY_OFFSET as ENTITY_KEY_OFFSET, ENTITY_KEY_WINDOW_OPEN_TEMPERATURE as ENTITY_KEY_WINDOW_OPEN_TEMPERATURE, ENTITY_KEY_WINDOW_OPEN_TIMEOUT as ENTITY_KEY_WINDOW_OPEN_TIMEOUT, EQ3BT_STEP as EQ3BT_STEP
from .entity import Eq3Entity as Eq3Entity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from eq3btsmart import Thermostat as Thermostat
from eq3btsmart.models import Presets as Presets
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class Eq3NumberEntityDescription(NumberEntityDescription):
    value_func: Callable[[Presets], float]
    value_set_func: Callable[[Thermostat], Callable[[float], Awaitable[None]]]
    mode: NumberMode = ...
    entity_category: EntityCategory | None = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., max_value=..., min_value=..., mode=..., native_max_value=..., native_min_value=..., native_step=..., native_unit_of_measurement=..., step=..., value_func, value_set_func) -> None: ...

NUMBER_ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: Eq3ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Eq3NumberEntity(Eq3Entity, NumberEntity):
    entity_description: Eq3NumberEntityDescription
    def __init__(self, entry: Eq3ConfigEntry, entity_description: Eq3NumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
    async def async_set_native_value(self, value: float) -> None: ...
    @property
    def available(self) -> bool: ...
