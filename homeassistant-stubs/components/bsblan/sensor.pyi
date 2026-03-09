from . import BSBLanConfigEntry as BSBLanConfigEntry, BSBLanData as BSBLanData
from .coordinator import BSBLanFastData as BSBLanFastData
from .entity import BSBLanEntity as BSBLanEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class BSBLanSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[BSBLanFastData], StateType]
    exists_fn: Callable[[BSBLanFastData], bool] = ...

SENSOR_TYPES: tuple[BSBLanSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: BSBLanConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BSBLanSensor(BSBLanEntity, SensorEntity):
    entity_description: BSBLanSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_temperature_unit: Incomplete
    def __init__(self, data: BSBLanData, description: BSBLanSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
