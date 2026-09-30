from .entity import MideaConfigEntry as MideaConfigEntry, MideaEntity as MideaEntity
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import EntityCategory as EntityCategory, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfDensity as UnitOfDensity, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfRatio as UnitOfRatio, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from midealocal.const import DeviceType
from typing import override

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class MideaSensorEntityDescription(SensorEntityDescription):
    models: list[DeviceType] | None = ...

SENSOR_ENTITIES: list[MideaSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MideaSensor(MideaEntity, SensorEntity):
    @property
    @override
    def native_value(self) -> StateType | datetime: ...
