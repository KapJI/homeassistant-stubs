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
from letpot.models import LetPotDeviceStatus as LetPotDeviceStatus, LetPotGardenStatus

PARALLEL_UPDATES: int
LETPOT_TEMPERATURE_UNIT_HA_UNIT: Incomplete

@dataclass(frozen=True, kw_only=True)
class LetPotSensorEntityDescription[_DataT: LetPotDeviceStatus](LetPotEntityDescription, SensorEntityDescription):
    native_unit_of_measurement_fn: Callable[[_DataT], str | None]
    value_fn: Callable[[_DataT], StateType]

SENSORS: tuple[LetPotSensorEntityDescription[LetPotGardenStatus], ...]

async def async_setup_entry(hass: HomeAssistant, entry: LetPotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LetPotSensorEntity[_DataT: LetPotDeviceStatus](LetPotEntity[_DataT], SensorEntity):
    entity_description: LetPotSensorEntityDescription[_DataT]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LetPotDeviceCoordinator[_DataT], description: LetPotSensorEntityDescription[_DataT]) -> None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> StateType: ...
