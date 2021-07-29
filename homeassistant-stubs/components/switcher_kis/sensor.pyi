from . import SwitcherDeviceWrapper as SwitcherDeviceWrapper
from .const import SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from homeassistant.components.sensor import DEVICE_CLASS_CURRENT as DEVICE_CLASS_CURRENT, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, POWER_WATT as POWER_WATT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as device_registry
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class AttributeDescription:
    name: str
    icon: Union[str, None]
    unit: Union[str, None]
    device_class: Union[str, None]
    state_class: Union[str, None]
    default_enabled: bool

POWER_SENSORS: Any
TIME_SENSORS: Any
POWER_PLUG_SENSORS = POWER_SENSORS
WATER_HEATER_SENSORS: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SwitcherSensorEntity(CoordinatorEntity, SensorEntity):
    wrapper: Any
    attribute: Any
    _attr_name: Any
    _attr_icon: Any
    _attr_unit_of_measurement: Any
    _attr_device_class: Any
    _attr_entity_registry_enabled_default: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, wrapper: SwitcherDeviceWrapper, attribute: str, description: AttributeDescription) -> None: ...
    @property
    def state(self) -> StateType: ...
