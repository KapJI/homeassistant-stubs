from .coordinator import ImmichConfigEntry as ImmichConfigEntry, ImmichData as ImmichData, ImmichDataUpdateCoordinator as ImmichDataUpdateCoordinator
from .entity import ImmichEntity as ImmichEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ImmichSensorEntityDescription(SensorEntityDescription):
    value: Callable[[ImmichData], StateType]
    is_suitable: Callable[[ImmichData], bool] = ...

SENSOR_TYPES: tuple[ImmichSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ImmichConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ImmichSensorEntity(ImmichEntity, SensorEntity):
    entity_description: ImmichSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ImmichDataUpdateCoordinator, description: ImmichSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
