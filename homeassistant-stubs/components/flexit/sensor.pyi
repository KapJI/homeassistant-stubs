from .coordinator import FlexitConfigEntry as FlexitConfigEntry, FlexitDataCoordinator as FlexitDataCoordinator
from .entity import FlexitEntity as FlexitEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from flexit_modbus import Measurements as Measurements
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import override

@dataclass(kw_only=True, frozen=True)
class FlexitSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Measurements], StateType]

SENSORS: tuple[FlexitSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FlexitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FlexitSensor(FlexitEntity, SensorEntity):
    entity_description: FlexitSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FlexitDataCoordinator, entity_description: FlexitSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
