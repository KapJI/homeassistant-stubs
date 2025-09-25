from . import BRouteConfigEntry as BRouteConfigEntry
from .const import ATTR_API_INSTANTANEOUS_CURRENT_R_PHASE as ATTR_API_INSTANTANEOUS_CURRENT_R_PHASE, ATTR_API_INSTANTANEOUS_CURRENT_T_PHASE as ATTR_API_INSTANTANEOUS_CURRENT_T_PHASE, ATTR_API_INSTANTANEOUS_POWER as ATTR_API_INSTANTANEOUS_POWER, ATTR_API_TOTAL_CONSUMPTION as ATTR_API_TOTAL_CONSUMPTION, DOMAIN as DOMAIN
from .coordinator import BRouteData as BRouteData, BRouteUpdateCoordinator as BRouteUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class SensorEntityDescriptionWithValueAccessor(SensorEntityDescription):
    value_accessor: Callable[[BRouteData], StateType]

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BRouteConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SmartMeterBRouteSensor(CoordinatorEntity[BRouteUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: SensorEntityDescriptionWithValueAccessor
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: BRouteUpdateCoordinator, description: SensorEntityDescriptionWithValueAccessor) -> None: ...
    @property
    def native_value(self) -> StateType: ...
