import aioshelly
from . import ShellyDeviceWrapper as ShellyDeviceWrapper
from .const import LAST_RESET_NEVER as LAST_RESET_NEVER, LAST_RESET_UPTIME as LAST_RESET_UPTIME, SHAIR_MAX_WORK_HOURS as SHAIR_MAX_WORK_HOURS
from .entity import BlockAttributeDescription as BlockAttributeDescription, RestAttributeDescription as RestAttributeDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rest as async_setup_entry_rest
from .utils import get_device_uptime as get_device_uptime, temperature_unit as temperature_unit
from homeassistant.components import sensor as sensor
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util import dt as dt
from typing import Any, Final

_LOGGER: Final[Any]
SENSORS: Final[Any]
REST_SENSORS: Final[Any]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ShellySensor(ShellyBlockAttributeEntity, SensorEntity):
    _last_value: Any
    _attr_last_reset: Any
    def __init__(self, wrapper: ShellyDeviceWrapper, block: aioshelly.Block, attribute: str, description: BlockAttributeDescription) -> None: ...
    @property
    def state(self) -> StateType: ...
    @property
    def state_class(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...

class ShellyRestSensor(ShellyRestAttributeEntity, SensorEntity):
    @property
    def state(self) -> StateType: ...
    @property
    def state_class(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...

class ShellySleepingSensor(ShellySleepingBlockAttributeEntity, SensorEntity):
    @property
    def state(self) -> StateType: ...
    @property
    def state_class(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
