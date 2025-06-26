from .coordinator import PaperlessConfigEntry as PaperlessConfigEntry, PaperlessCoordinator as PaperlessCoordinator, PaperlessStatisticCoordinator as PaperlessStatisticCoordinator, PaperlessStatusCoordinator as PaperlessStatusCoordinator
from .entity import PaperlessEntity as PaperlessEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.unit_conversion import InformationConverter as InformationConverter
from pypaperless.models import Statistic, Status

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PaperlessEntityDescription[DataT](SensorEntityDescription):
    value_fn: Callable[[DataT], StateType]

SENSOR_STATISTICS: tuple[PaperlessEntityDescription[Statistic], ...]
SENSOR_STATUS: tuple[PaperlessEntityDescription[Status], ...]

async def async_setup_entry(hass: HomeAssistant, entry: PaperlessConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PaperlessSensor[CoordinatorT: PaperlessCoordinator](PaperlessEntity[CoordinatorT], SensorEntity):
    entity_description: PaperlessEntityDescription
    @property
    def native_value(self) -> StateType: ...
