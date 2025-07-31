from .const import DOMAIN as DOMAIN
from .coordinator import OpowerConfigEntry as OpowerConfigEntry, OpowerCoordinator as OpowerCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import date
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfEnergy as UnitOfEnergy, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from opower import Forecast as Forecast

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OpowerEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Forecast], str | float | date]

ELEC_SENSORS: tuple[OpowerEntityDescription, ...]
GAS_SENSORS: tuple[OpowerEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpowerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpowerSensor(CoordinatorEntity[OpowerCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: OpowerEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    utility_account_id: Incomplete
    def __init__(self, coordinator: OpowerCoordinator, description: OpowerEntityDescription, utility_account_id: str, device: DeviceInfo, device_id: str) -> None: ...
    @property
    def native_value(self) -> StateType | date: ...
