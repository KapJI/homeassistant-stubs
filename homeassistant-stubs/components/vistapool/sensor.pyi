from . import VistapoolConfigEntry as VistapoolConfigEntry
from .const import PATH_HASCD as PATH_HASCD, PATH_HASCL as PATH_HASCL, PATH_HASHIDRO as PATH_HASHIDRO, PATH_HASPH as PATH_HASPH, PATH_HASRX as PATH_HASRX, PATH_HASUV as PATH_HASUV
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from .entity import VistapoolEntity as VistapoolEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

def _convert_hundredths(value: Any) -> float: ...
def _convert_tenths(value: Any) -> float: ...

@dataclass(frozen=True, kw_only=True)
class VistapoolSensorEntityDescription(SensorEntityDescription):
    value_path: str
    value_fn: Callable[[Any], float | int] = ...
    exists_path: str | None = ...

SENSOR_DESCRIPTIONS: tuple[VistapoolSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VistapoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VistapoolSensorEntity(VistapoolEntity, SensorEntity):
    entity_description: VistapoolSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VistapoolDataUpdateCoordinator, description: VistapoolSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> float | int | None: ...
