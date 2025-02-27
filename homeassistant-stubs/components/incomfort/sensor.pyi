from .coordinator import InComfortConfigEntry as InComfortConfigEntry, InComfortDataCoordinator as InComfortDataCoordinator
from .entity import IncomfortBoilerEntity as IncomfortBoilerEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from incomfortclient import Heater as InComfortHeater
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IncomfortSensorEntityDescription(SensorEntityDescription):
    value_key: str
    extra_key: str | None = ...
    entity_category = ...

SENSOR_TYPES: tuple[IncomfortSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: InComfortConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IncomfortSensor(IncomfortBoilerEntity, SensorEntity):
    entity_description: IncomfortSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: InComfortDataCoordinator, heater: InComfortHeater, description: IncomfortSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
