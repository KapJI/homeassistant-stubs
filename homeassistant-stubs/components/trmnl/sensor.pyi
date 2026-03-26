from . import TRMNLConfigEntry as TRMNLConfigEntry
from .coordinator import TRMNLCoordinator as TRMNLCoordinator
from .entity import TRMNLEntity as TRMNLEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricPotential as UnitOfElectricPotential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from trmnl.models import Device as Device

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TRMNLSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Device], int | float | None]

SENSOR_DESCRIPTIONS: tuple[TRMNLSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TRMNLConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TRMNLSensor(TRMNLEntity, SensorEntity):
    entity_description: TRMNLSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: TRMNLCoordinator, device_id: int, description: TRMNLSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | float | None: ...
