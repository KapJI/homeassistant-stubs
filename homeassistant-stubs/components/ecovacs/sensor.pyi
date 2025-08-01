from . import EcovacsConfigEntry as EcovacsConfigEntry
from .const import LEGACY_SUPPORTED_LIFESPANS as LEGACY_SUPPORTED_LIFESPANS, SUPPORTED_LIFESPANS as SUPPORTED_LIFESPANS
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity, EcovacsLegacyEntity as EcovacsLegacyEntity
from .util import get_name_key as get_name_key, get_options as get_options, get_supported_entities as get_supported_entities
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from deebot_client.capabilities import CapabilityEvent, CapabilityLifeSpan, DeviceType
from deebot_client.device import Device as Device
from deebot_client.events import ErrorEvent, Event as Event, LifeSpan as LifeSpan, LifeSpanEvent as LifeSpanEvent
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_BATTERY_LEVEL as ATTR_BATTERY_LEVEL, CONF_DESCRIPTION as CONF_DESCRIPTION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfArea as UnitOfArea, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.typing import StateType as StateType
from sucks import VacBot as VacBot
from typing import Any

@dataclass(kw_only=True, frozen=True)
class EcovacsSensorEntityDescription[EventT: Event](EcovacsCapabilityEntityDescription, SensorEntityDescription):
    value_fn: Callable[[EventT], StateType]
    native_unit_of_measurement_fn: Callable[[DeviceType], str | None] | None = ...

@callback
def get_area_native_unit_of_measurement(device_type: DeviceType) -> str | None: ...

ENTITY_DESCRIPTIONS: tuple[EcovacsSensorEntityDescription, ...]

@dataclass(kw_only=True, frozen=True)
class EcovacsLifespanSensorEntityDescription(SensorEntityDescription):
    component: LifeSpan
    value_fn: Callable[[LifeSpanEvent], int | float]

LIFESPAN_ENTITY_DESCRIPTIONS: Incomplete

@dataclass(kw_only=True, frozen=True)
class EcovacsLegacyLifespanSensorEntityDescription(SensorEntityDescription):
    component: str

LEGACY_LIFESPAN_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EcovacsSensor(EcovacsDescriptionEntity[CapabilityEvent], SensorEntity):
    entity_description: EcovacsSensorEntityDescription
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, device: Device, capability: CapabilityEvent, entity_description: EcovacsSensorEntityDescription, **kwargs: Any) -> None: ...
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

class EcovacsLegacyBatterySensor(EcovacsLegacyEntity, SensorEntity):
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: VacBot) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def icon(self) -> str | None: ...

class EcovacsLegacyLifespanSensor(EcovacsLegacyEntity, SensorEntity):
    entity_description: EcovacsLegacyLifespanSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, device: VacBot, description: EcovacsLegacyLifespanSensorEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
