from . import BesenConfigEntry as BesenConfigEntry
from .coordinator import BesenCoordinator as BesenCoordinator
from .entity import BesenEntity as BesenEntity
from _typeshed import Incomplete
from besen.models import BesenData as BesenData
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final, override

PARALLEL_UPDATES: int
ERROR_STATES: Final[Incomplete]
CHARGING_STATES: Final[Incomplete]
CHARGING_MESSAGES: Final[Incomplete]
PLUG_STATES: Final[Incomplete]
OUTPUT_STATES: Final[Incomplete]
CURRENT_STATES: Final[Incomplete]

def _enum_state(value: str | None, states: Mapping[str, str]) -> str | None: ...

@dataclass(frozen=True, kw_only=True)
class BesenSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[BesenData], StateType]
    three_phase_only: bool = ...

SENSOR_DESCRIPTIONS: tuple[BesenSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: BesenConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BesenSensor(BesenEntity, SensorEntity):
    entity_description: BesenSensorEntityDescription
    def __init__(self, coordinator: BesenCoordinator, description: BesenSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
