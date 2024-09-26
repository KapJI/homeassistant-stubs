from . import SolarlogConfigEntry as SolarlogConfigEntry
from .entity import SolarLogCoordinatorEntity as SolarLogCoordinatorEntity, SolarLogInverterEntity as SolarLogInverterEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from solarlog_cli.solarlog_models import InverterData as InverterData, SolarlogData as SolarlogData

@dataclass(frozen=True, kw_only=True)
class SolarLogCoordinatorSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SolarlogData], StateType | datetime | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

@dataclass(frozen=True, kw_only=True)
class SolarLogInverterSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[InverterData], float | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

SOLARLOG_SENSOR_TYPES: tuple[SolarLogCoordinatorSensorEntityDescription, ...]
INVERTER_SENSOR_TYPES: tuple[SolarLogInverterSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SolarlogConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SolarLogCoordinatorSensor(SolarLogCoordinatorEntity, SensorEntity):
    entity_description: SolarLogCoordinatorSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...

class SolarLogInverterSensor(SolarLogInverterEntity, SensorEntity):
    entity_description: SolarLogInverterSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
