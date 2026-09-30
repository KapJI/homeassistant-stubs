from .coordinator import SunsynkConfigEntry as SunsynkConfigEntry, SunsynkInverterData as SunsynkInverterData
from .entity import SunsynkBatteryEntity as SunsynkBatteryEntity, SunsynkInverterEntity as SunsynkInverterEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import override

@dataclass(frozen=True, kw_only=True)
class SunsynkSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SunsynkInverterData], StateType]

SENSORS_INVERTER: tuple[SunsynkSensorEntityDescription, ...]
SENSORS_BATTERY: tuple[SunsynkSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SunsynkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SunsynkInverterSensorEntity(SunsynkInverterEntity, SensorEntity):
    entity_description: SunsynkSensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType: ...

class SunsynkBatterySensorEntity(SunsynkBatteryEntity, SensorEntity):
    entity_description: SunsynkSensorEntityDescription
    @property
    @override
    def native_value(self) -> StateType: ...
