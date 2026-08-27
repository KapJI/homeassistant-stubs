from .coordinator import ActronAirConfigEntry as ActronAirConfigEntry, ActronAirSystemCoordinator as ActronAirSystemCoordinator
from .entity import ActronAirAcEntity as ActronAirAcEntity, ActronAirPeripheralEntity as ActronAirPeripheralEntity
from _typeshed import Incomplete
from actron_neo_api import ActronAirStatus as ActronAirStatus
from actron_neo_api.models.zone import ActronAirPeripheral as ActronAirPeripheral
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ActronAirSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[ActronAirStatus], str | float | int | None]

@dataclass(frozen=True, kw_only=True)
class ActronAirPeripheralSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[ActronAirPeripheral], float | None]

SENSORS: tuple[ActronAirSensorEntityDescription, ...]
PERIPHERAL_SENSORS: tuple[ActronAirPeripheralSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ActronAirConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ActronAirSensor(ActronAirAcEntity, SensorEntity):
    entity_description: ActronAirSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ActronAirSystemCoordinator, description: ActronAirSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> str | float | int | None: ...

class ActronAirPeripheralSensor(ActronAirPeripheralEntity, SensorEntity):
    entity_description: ActronAirPeripheralSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ActronAirSystemCoordinator, peripheral: ActronAirPeripheral, description: ActronAirPeripheralSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> float | None: ...
