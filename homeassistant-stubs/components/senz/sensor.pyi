from . import SENZConfigEntry as SENZConfigEntry, SENZDataUpdateCoordinator as SENZDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiosenz import Thermostat as Thermostat
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(kw_only=True, frozen=True)
class SenzSensorDescription(SensorEntityDescription):
    value_fn: Callable[[Thermostat], str | int | float | None]

SENSORS: tuple[SenzSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SENZConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SENZSensor(CoordinatorEntity[SENZDataUpdateCoordinator], SensorEntity):
    entity_description: SenzSensorDescription
    _attr_has_entity_name: bool
    _thermostat: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, thermostat: Thermostat, coordinator: SENZDataUpdateCoordinator, description: SenzSensorDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> str | float | int | None: ...
