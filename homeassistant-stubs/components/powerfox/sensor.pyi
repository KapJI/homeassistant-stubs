from . import PowerfoxConfigEntry as PowerfoxConfigEntry
from .coordinator import PowerfoxDataUpdateCoordinator as PowerfoxDataUpdateCoordinator
from .entity import PowerfoxEntity as PowerfoxEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from powerfox import Device as Device, PowerMeter, WaterMeter

@dataclass(frozen=True, kw_only=True)
class PowerfoxSensorEntityDescription[T: (PowerMeter, WaterMeter)](SensorEntityDescription):
    value_fn: Callable[[T], float | int | None]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

SENSORS_POWER: tuple[PowerfoxSensorEntityDescription[PowerMeter], ...]
SENSORS_WATER: tuple[PowerfoxSensorEntityDescription[WaterMeter], ...]

async def async_setup_entry(hass: HomeAssistant, entry: PowerfoxConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PowerfoxSensorEntity(PowerfoxEntity, SensorEntity):
    entity_description: PowerfoxSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PowerfoxDataUpdateCoordinator, device: Device, description: PowerfoxSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
