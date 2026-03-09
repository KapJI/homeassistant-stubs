from .coordinator import AirOS8Data as AirOS8Data, AirOSConfigEntry as AirOSConfigEntry, AirOSDataUpdateCoordinator as AirOSDataUpdateCoordinator
from .entity import AirOSEntity as AirOSEntity
from _typeshed import Incomplete
from airos.data import AirOSDataBaseClass
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfDataRate as UnitOfDataRate, UnitOfFrequency as UnitOfFrequency, UnitOfLength as UnitOfLength, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Generic, TypeVar

_LOGGER: Incomplete
NETROLE_OPTIONS: Incomplete
WIRELESS_MODE_OPTIONS: Incomplete
WIRELESS_ROLE_OPTIONS: Incomplete
PARALLEL_UPDATES: int
AirOSDataModel = TypeVar('AirOSDataModel', bound=AirOSDataBaseClass)

@dataclass(frozen=True, kw_only=True)
class AirOSSensorEntityDescription(SensorEntityDescription, Generic[AirOSDataModel]):
    value_fn: Callable[[AirOSDataModel], StateType]
AirOS8SensorEntityDescription = AirOSSensorEntityDescription[AirOS8Data]
COMMON_SENSORS: tuple[AirOSSensorEntityDescription, ...]
AIROS8_SENSORS: tuple[AirOS8SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: AirOSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirOSSensor(AirOSEntity, SensorEntity):
    entity_description: AirOSSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirOSDataUpdateCoordinator, description: AirOSSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
