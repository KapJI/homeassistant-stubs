import datetime
from .const import DOMAIN as DOMAIN
from .coordinator import EnphaseUpdateCoordinator as EnphaseUpdateCoordinator
from .entity import EnvoyBaseEntity as EnvoyBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfApparentPower as UnitOfApparentPower, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyenphase import EnvoyEncharge as EnvoyEncharge, EnvoyEnchargeAggregate as EnvoyEnchargeAggregate, EnvoyEnchargePower as EnvoyEnchargePower, EnvoyEnpower as EnvoyEnpower, EnvoyInverter as EnvoyInverter, EnvoySystemConsumption as EnvoySystemConsumption, EnvoySystemProduction as EnvoySystemProduction
from pyenphase.const import PhaseNames

ICON: str
_LOGGER: Incomplete
INVERTERS_KEY: str
LAST_REPORTED_KEY: str

@dataclass(frozen=True)
class EnvoyInverterRequiredKeysMixin:
    value_fn: Callable[[EnvoyInverter], datetime.datetime | float]
    def __init__(self, value_fn) -> None: ...

@dataclass(frozen=True)
class EnvoyInverterSensorEntityDescription(SensorEntityDescription, EnvoyInverterRequiredKeysMixin):
    def __init__(self, value_fn, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

INVERTER_SENSORS: Incomplete

@dataclass(frozen=True)
class EnvoyProductionRequiredKeysMixin:
    value_fn: Callable[[EnvoySystemProduction], int]
    on_phase: PhaseNames | None
    def __init__(self, value_fn, on_phase) -> None: ...

@dataclass(frozen=True)
class EnvoyProductionSensorEntityDescription(SensorEntityDescription, EnvoyProductionRequiredKeysMixin):
    def __init__(self, value_fn, on_phase, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

PRODUCTION_SENSORS: Incomplete
PRODUCTION_PHASE_SENSORS: Incomplete

@dataclass(frozen=True)
class EnvoyConsumptionRequiredKeysMixin:
    value_fn: Callable[[EnvoySystemConsumption], int]
    on_phase: PhaseNames | None
    def __init__(self, value_fn, on_phase) -> None: ...

@dataclass(frozen=True)
class EnvoyConsumptionSensorEntityDescription(SensorEntityDescription, EnvoyConsumptionRequiredKeysMixin):
    def __init__(self, value_fn, on_phase, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

CONSUMPTION_SENSORS: Incomplete
CONSUMPTION_PHASE_SENSORS: Incomplete

@dataclass(frozen=True)
class EnvoyEnchargeRequiredKeysMixin:
    value_fn: Callable[[EnvoyEncharge], datetime.datetime | int | float]
    def __init__(self, value_fn) -> None: ...

@dataclass(frozen=True)
class EnvoyEnchargeSensorEntityDescription(SensorEntityDescription, EnvoyEnchargeRequiredKeysMixin):
    def __init__(self, value_fn, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

@dataclass(frozen=True)
class EnvoyEnchargePowerRequiredKeysMixin:
    value_fn: Callable[[EnvoyEnchargePower], int | float]
    def __init__(self, value_fn) -> None: ...

@dataclass(frozen=True)
class EnvoyEnchargePowerSensorEntityDescription(SensorEntityDescription, EnvoyEnchargePowerRequiredKeysMixin):
    def __init__(self, value_fn, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

ENCHARGE_INVENTORY_SENSORS: Incomplete
ENCHARGE_POWER_SENSORS: Incomplete

@dataclass(frozen=True)
class EnvoyEnpowerRequiredKeysMixin:
    value_fn: Callable[[EnvoyEnpower], datetime.datetime | int | float]
    def __init__(self, value_fn) -> None: ...

@dataclass(frozen=True)
class EnvoyEnpowerSensorEntityDescription(SensorEntityDescription, EnvoyEnpowerRequiredKeysMixin):
    def __init__(self, value_fn, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

ENPOWER_SENSORS: Incomplete

@dataclass(frozen=True)
class EnvoyEnchargeAggregateRequiredKeysMixin:
    value_fn: Callable[[EnvoyEnchargeAggregate], int]
    def __init__(self, value_fn) -> None: ...

@dataclass(frozen=True)
class EnvoyEnchargeAggregateSensorEntityDescription(SensorEntityDescription, EnvoyEnchargeAggregateRequiredKeysMixin):
    def __init__(self, value_fn, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

ENCHARGE_AGGREGATE_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EnvoySensorBaseEntity(EnvoyBaseEntity, SensorEntity): ...

class EnvoySystemSensorEntity(EnvoySensorBaseEntity):
    _attr_icon = ICON
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: SensorEntityDescription) -> None: ...

class EnvoyProductionEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyProductionSensorEntityDescription
    @property
    def native_value(self) -> int | None: ...

class EnvoyConsumptionEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyConsumptionSensorEntityDescription
    @property
    def native_value(self) -> int | None: ...

class EnvoyProductionPhaseEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyProductionSensorEntityDescription
    @property
    def native_value(self) -> int | None: ...

class EnvoyConsumptionPhaseEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyConsumptionSensorEntityDescription
    @property
    def native_value(self) -> int | None: ...

class EnvoyInverterEntity(EnvoySensorBaseEntity):
    _attr_icon = ICON
    entity_description: EnvoyInverterSensorEntityDescription
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyInverterSensorEntityDescription, serial_number: str) -> None: ...
    @property
    def native_value(self) -> datetime.datetime | float | None: ...

class EnvoyEnchargeEntity(EnvoySensorBaseEntity):
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyEnchargeSensorEntityDescription | EnvoyEnchargePowerSensorEntityDescription, serial_number: str) -> None: ...

class EnvoyEnchargeInventoryEntity(EnvoyEnchargeEntity):
    entity_description: EnvoyEnchargeSensorEntityDescription
    @property
    def native_value(self) -> int | float | datetime.datetime | None: ...

class EnvoyEnchargePowerEntity(EnvoyEnchargeEntity):
    entity_description: EnvoyEnchargePowerSensorEntityDescription
    @property
    def native_value(self) -> int | float | None: ...

class EnvoyEnchargeAggregateEntity(EnvoySystemSensorEntity):
    entity_description: EnvoyEnchargeAggregateSensorEntityDescription
    @property
    def native_value(self) -> int: ...

class EnvoyEnpowerEntity(EnvoySensorBaseEntity):
    entity_description: EnvoyEnpowerSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: EnphaseUpdateCoordinator, description: EnvoyEnpowerSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime.datetime | int | float | None: ...
