from .coordinator import KacoConfigEntry as KacoConfigEntry
from .entity import KacoEntity as KacoEntity, KacoEntityDescription as KacoEntityDescription
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from kaco_modbus.models import InverterThreePhase as InverterThreePhase
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class KacoSensorDescription(SensorEntityDescription, KacoEntityDescription):
    value_fn: Callable[[InverterThreePhase], StateType]

SENSOR_DESCRIPTIONS: tuple[KacoSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: KacoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class KacoSensor(KacoEntity, SensorEntity):
    entity_description: KacoSensorDescription
    @property
    @override
    def native_value(self) -> StateType: ...
