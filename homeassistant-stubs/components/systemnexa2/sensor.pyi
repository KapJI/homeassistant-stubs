from .coordinator import SystemNexa2ConfigEntry as SystemNexa2ConfigEntry, SystemNexa2DataUpdateCoordinator as SystemNexa2DataUpdateCoordinator
from .entity import SystemNexa2Entity as SystemNexa2Entity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class SystemNexa2SensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SystemNexa2DataUpdateCoordinator], str | int | None]

SENSOR_DESCRIPTIONS: tuple[SystemNexa2SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SystemNexa2ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SystemNexa2Sensor(SystemNexa2Entity, SensorEntity):
    entity_description: SystemNexa2SensorEntityDescription
    def __init__(self, coordinator: SystemNexa2DataUpdateCoordinator, entity_description: SystemNexa2SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> str | int | None: ...
