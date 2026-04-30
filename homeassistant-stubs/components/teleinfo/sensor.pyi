from .const import DOMAIN as DOMAIN
from .coordinator import TeleinfoConfigEntry as TeleinfoConfigEntry, TeleinfoCoordinator as TeleinfoCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfEnergy as UnitOfEnergy, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int
PTEC_OPTIONS: dict[str, str]
DEMAIN_OPTIONS: dict[str, str | None]

@dataclass(frozen=True, kw_only=True)
class TeleinfoSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[str], StateType] = ...

SENSOR_DESCRIPTIONS: tuple[TeleinfoSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TeleinfoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeleinfoSensor(CoordinatorEntity[TeleinfoCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: TeleinfoSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TeleinfoCoordinator, description: TeleinfoSensorEntityDescription, adco: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
