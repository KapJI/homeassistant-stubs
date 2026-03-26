from . import QubeConfigEntry as QubeConfigEntry
from .coordinator import QubeCoordinator as QubeCoordinator
from .entity import QubeEntity as QubeEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from python_qube_heatpump.models import QubeState as QubeState

PARALLEL_UPDATES: int
STATUS_MAP: dict[int, str]

@dataclass(frozen=True, kw_only=True)
class QubeSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[QubeState], StateType]

def _status_value(data: QubeState) -> StateType: ...

SENSOR_TYPES: tuple[QubeSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: QubeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QubeSensor(QubeEntity, SensorEntity):
    entity_description: QubeSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: QubeCoordinator, entry: QubeConfigEntry, description: QubeSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
