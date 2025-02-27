from .coordinator import LetPotConfigEntry as LetPotConfigEntry, LetPotDeviceCoordinator as LetPotDeviceCoordinator
from .entity import LetPotEntity as LetPotEntity, LetPotEntityDescription as LetPotEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from letpot.models import LetPotDeviceStatus as LetPotDeviceStatus

PARALLEL_UPDATES: int
LETPOT_TEMPERATURE_UNIT_HA_UNIT: Incomplete

@dataclass(frozen=True, kw_only=True)
class LetPotSensorEntityDescription(LetPotEntityDescription, SensorEntityDescription):
    native_unit_of_measurement_fn: Callable[[LetPotDeviceStatus], str | None]
    value_fn: Callable[[LetPotDeviceStatus], StateType]

SENSORS: tuple[LetPotSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LetPotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LetPotSensorEntity(LetPotEntity, SensorEntity):
    entity_description: LetPotSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LetPotDeviceCoordinator, description: LetPotSensorEntityDescription) -> None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> StateType: ...
