from . import SwitcherDataUpdateCoordinator as SwitcherDataUpdateCoordinator
from .const import SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AttributeDescription:
    name: str
    icon: str | None
    unit: str | None
    device_class: SensorDeviceClass | None
    state_class: SensorStateClass | None
    default_enabled: bool
    def __init__(self, name, icon, unit, device_class, state_class, default_enabled) -> None: ...

POWER_SENSORS: Incomplete
TIME_SENSORS: Incomplete
POWER_PLUG_SENSORS = POWER_SENSORS
WATER_HEATER_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherSensorEntity(CoordinatorEntity[SwitcherDataUpdateCoordinator], SensorEntity):
    attribute: Incomplete
    _attr_name: Incomplete
    _attr_icon: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_device_class: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SwitcherDataUpdateCoordinator, attribute: str, description: AttributeDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
