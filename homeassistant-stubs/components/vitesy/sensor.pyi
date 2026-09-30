from .const import LOGGER as LOGGER
from .coordinator import VitesyConfigEntry as VitesyConfigEntry, VitesyDataUpdateCoordinator as VitesyDataUpdateCoordinator
from .entity import VitesyEntity as VitesyEntity
from _typeshed import Incomplete
from aiovitesy.api import VitesyDevice as VitesyDevice
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import override

PARALLEL_UPDATES: int
_SENSORS_DATA: str
_STATUS_DATA: str
_FRIDGE_TEMPERATURE: str
_DOOR_OPENINGS: str
_DOOR_OPEN_DURATION: str
_BATTERY: str

def _reading(device: VitesyDevice, group: str, reading_id: str) -> float | None: ...
def _air_quality_score(device: VitesyDevice) -> float | None: ...
def _maintenance_due(component: str) -> Callable[[VitesyDevice], datetime | None]: ...

@dataclass(frozen=True, kw_only=True)
class VitesySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[VitesyDevice], StateType | datetime]

SENSORS: tuple[VitesySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VitesyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VitesySensor(VitesyEntity, SensorEntity):
    entity_description: VitesySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VitesyDataUpdateCoordinator, device_id: str, description: VitesySensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType | datetime: ...
