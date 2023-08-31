from . import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from .const import SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

POWER_SENSORS: list[SensorEntityDescription]
TIME_SENSORS: list[SensorEntityDescription]
POWER_PLUG_SENSORS = POWER_SENSORS
WATER_HEATER_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherSensorEntity(CoordinatorEntity[SwitcherDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
