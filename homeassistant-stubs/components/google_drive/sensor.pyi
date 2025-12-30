from .coordinator import GoogleDriveConfigEntry as GoogleDriveConfigEntry, GoogleDriveDataUpdateCoordinator as GoogleDriveDataUpdateCoordinator, SensorData as SensorData
from .entity import GoogleDriveEntity as GoogleDriveEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfInformation as UnitOfInformation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class GoogleDriveSensorEntityDescription(SensorEntityDescription):
    exists_fn: Callable[[SensorData], bool] = ...
    value_fn: Callable[[SensorData], StateType]

SENSORS: tuple[GoogleDriveSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: GoogleDriveConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GoogleDriveSensorEntity(GoogleDriveEntity, SensorEntity):
    entity_description: GoogleDriveSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: GoogleDriveDataUpdateCoordinator, description: GoogleDriveSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
