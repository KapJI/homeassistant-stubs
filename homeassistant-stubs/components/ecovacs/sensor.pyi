from . import EcovacsConfigEntry as EcovacsConfigEntry
from .const import LEGACY_SUPPORTED_LIFESPANS as LEGACY_SUPPORTED_LIFESPANS, SUPPORTED_LIFESPANS as SUPPORTED_LIFESPANS
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity, EcovacsLegacyEntity as EcovacsLegacyEntity, EventT as EventT
from .util import get_supported_entitites as get_supported_entitites
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from deebot_client.capabilities import CapabilityEvent, CapabilityLifeSpan
from deebot_client.events import ErrorEvent, Event as Event, LifeSpan as LifeSpan, LifeSpanEvent as LifeSpanEvent
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import AREA_SQUARE_METERS as AREA_SQUARE_METERS, ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, CONF_DESCRIPTION as CONF_DESCRIPTION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from sucks import VacBot as VacBot
from typing import Generic

@dataclass(kw_only=True, frozen=True)
class EcovacsSensorEntityDescription(EcovacsCapabilityEntityDescription, SensorEntityDescription, Generic[EventT]):
    value_fn: Callable[[EventT], StateType]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., capability_fn, value_fn) -> None: ...

ENTITY_DESCRIPTIONS: tuple[EcovacsSensorEntityDescription, ...]

@dataclass(kw_only=True, frozen=True)
class EcovacsLifespanSensorEntityDescription(SensorEntityDescription):
    component: LifeSpan
    value_fn: Callable[[LifeSpanEvent], int | float]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., component, value_fn) -> None: ...

LIFESPAN_ENTITY_DESCRIPTIONS: Incomplete

@dataclass(kw_only=True, frozen=True)
class EcovacsLegacyLifespanSensorEntityDescription(SensorEntityDescription):
    component: str
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., component) -> None: ...

LEGACY_LIFESPAN_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsSensor(EcovacsDescriptionEntity[CapabilityEvent], SensorEntity):
    entity_description: EcovacsSensorEntityDescription
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...

class EcovacsLifespanSensor(EcovacsDescriptionEntity[CapabilityLifeSpan], SensorEntity):
    entity_description: EcovacsLifespanSensorEntityDescription
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...

class EcovacsErrorSensor(EcovacsEntity[CapabilityEvent[ErrorEvent]], SensorEntity):
    _always_available: bool
    _unrecorded_attributes: Incomplete
    entity_description: SensorEntityDescription
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    async def async_added_to_hass(self) -> None: ...

class EcovacsLegacyLifespanSensor(EcovacsLegacyEntity, SensorEntity):
    entity_description: EcovacsLegacyLifespanSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, device: VacBot, description: EcovacsLegacyLifespanSensorEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
