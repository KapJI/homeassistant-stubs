from .coordinator import PowerfoxConfigEntry as PowerfoxConfigEntry, PowerfoxDataUpdateCoordinator as PowerfoxDataUpdateCoordinator
from .entity import PowerfoxEntity as PowerfoxEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from powerfox import Device as Device, HeatMeter, PowerMeter, WaterMeter

@dataclass(frozen=True, kw_only=True)
class PowerfoxSensorEntityDescription[T: (PowerMeter, WaterMeter, HeatMeter)](SensorEntityDescription):
    value_fn: Callable[[T], float | int | None]

SENSORS_POWER: tuple[PowerfoxSensorEntityDescription[PowerMeter], ...]
SENSORS_WATER: tuple[PowerfoxSensorEntityDescription[WaterMeter], ...]
SENSORS_HEAT: tuple[PowerfoxSensorEntityDescription[HeatMeter], ...]

async def async_setup_entry(hass: HomeAssistant, entry: PowerfoxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PowerfoxSensorEntity(PowerfoxEntity, SensorEntity):
    entity_description: PowerfoxSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PowerfoxDataUpdateCoordinator, device: Device, description: PowerfoxSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
