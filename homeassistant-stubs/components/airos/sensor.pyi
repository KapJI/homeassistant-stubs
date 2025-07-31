from .coordinator import AirOSConfigEntry as AirOSConfigEntry, AirOSData as AirOSData, AirOSDataUpdateCoordinator as AirOSDataUpdateCoordinator
from .entity import AirOSEntity as AirOSEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfDataRate as UnitOfDataRate, UnitOfFrequency as UnitOfFrequency
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

_LOGGER: Incomplete
WIRELESS_MODE_OPTIONS: Incomplete
NETROLE_OPTIONS: Incomplete

@dataclass(frozen=True, kw_only=True)
class AirOSSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[AirOSData], StateType]

SENSORS: tuple[AirOSSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: AirOSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirOSSensor(AirOSEntity, SensorEntity):
    entity_description: AirOSSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirOSDataUpdateCoordinator, description: AirOSSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
