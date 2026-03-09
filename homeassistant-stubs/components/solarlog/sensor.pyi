from .coordinator import SolarlogConfigEntry as SolarlogConfigEntry
from .entity import SolarLogBasicCoordinatorEntity as SolarLogBasicCoordinatorEntity, SolarLogInverterEntity as SolarLogInverterEntity, SolarLogLongtimeCoordinatorEntity as SolarLogLongtimeCoordinatorEntity
from .models import SolarlogIntegrationData as SolarlogIntegrationData
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from solarlog_cli.solarlog_models import BatteryData as BatteryData, EnergyData as EnergyData, InverterData as InverterData, SolarlogData as SolarlogData

@dataclass(frozen=True, kw_only=True)
class SolarLogCoordinatorSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SolarlogData], StateType | datetime | None]

@dataclass(frozen=True, kw_only=True)
class SolarLogLongtimeSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[EnergyData], float | None]

@dataclass(frozen=True, kw_only=True)
class SolarLogBatterySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[BatteryData], float | int | None]

@dataclass(frozen=True, kw_only=True)
class SolarLogInverterSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[InverterData], float | None]

SOLARLOG_BASIC_SENSOR_TYPES: tuple[SolarLogCoordinatorSensorEntityDescription, ...]
SOLARLOG_LONGTIME_SENSOR_TYPES: tuple[SolarLogLongtimeSensorEntityDescription, ...]
SOLARLOG_BATTERY_SENSOR_TYPES: tuple[SolarLogBatterySensorEntityDescription, ...]
SOLARLOG_INVERTER_SENSOR_TYPES: tuple[SolarLogInverterSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SolarlogConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SolarLogBasicCoordinatorSensor(SolarLogBasicCoordinatorEntity, SensorEntity):
    entity_description: SolarLogCoordinatorSensorEntityDescription
    @property
    def native_value(self) -> StateType | datetime: ...

class SolarLogLongtimeCoordinatorSensor(SolarLogLongtimeCoordinatorEntity, SensorEntity):
    entity_description: SolarLogLongtimeSensorEntityDescription
    @property
    def native_value(self) -> float | None: ...

class SolarLogBatterySensor(SolarLogBasicCoordinatorEntity, SensorEntity):
    entity_description: SolarLogBatterySensorEntityDescription
    @property
    def native_value(self) -> StateType: ...

class SolarLogInverterSensor(SolarLogInverterEntity, SensorEntity):
    entity_description: SolarLogInverterSensorEntityDescription
    @property
    def native_value(self) -> StateType: ...
