from .coordinator import PaperlessConfigEntry as PaperlessConfigEntry, PaperlessStatisticCoordinator as PaperlessStatisticCoordinator, PaperlessStatusCoordinator as PaperlessStatusCoordinator, TData as TData
from .entity import PaperlessEntity as PaperlessEntity, TCoordinator as TCoordinator
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.unit_conversion import InformationConverter as InformationConverter
from typing import Generic

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PaperlessEntityDescription(SensorEntityDescription, Generic[TData]):
    value_fn: Callable[[TData], StateType]

SENSOR_STATISTICS: tuple[PaperlessEntityDescription, ...]
SENSOR_STATUS: tuple[PaperlessEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PaperlessConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PaperlessSensor(PaperlessEntity[TCoordinator], SensorEntity):
    entity_description: PaperlessEntityDescription
    @property
    def native_value(self) -> StateType: ...
