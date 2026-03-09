from .coordinator import PowerfoxLocalConfigEntry as PowerfoxLocalConfigEntry, PowerfoxLocalDataUpdateCoordinator as PowerfoxLocalDataUpdateCoordinator
from .entity import PowerfoxLocalEntity as PowerfoxLocalEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from powerfox import LocalResponse as LocalResponse

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class PowerfoxLocalSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[LocalResponse], float | int | None]

SENSORS: tuple[PowerfoxLocalSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PowerfoxLocalConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PowerfoxLocalSensorEntity(PowerfoxLocalEntity, SensorEntity):
    entity_description: PowerfoxLocalSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PowerfoxLocalDataUpdateCoordinator, description: PowerfoxLocalSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
