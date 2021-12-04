from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, SHAIR_MAX_WORK_HOURS as SHAIR_MAX_WORK_HOURS
from .entity import BlockAttributeDescription as BlockAttributeDescription, RestAttributeDescription as RestAttributeDescription, RpcAttributeDescription as RpcAttributeDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rest as async_setup_entry_rest, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import get_device_entry_gen as get_device_entry_gen, get_device_uptime as get_device_uptime, temperature_unit as temperature_unit
from homeassistant.components import sensor as sensor
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, Final

SENSORS: Final[Any]
REST_SENSORS: Final[Any]
RPC_SENSORS: Final[Any]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockSensor(ShellyBlockAttributeEntity, SensorEntity):
    @property
    def native_value(self) -> StateType: ...
    @property
    def state_class(self) -> Union[str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...

class RestSensor(ShellyRestAttributeEntity, SensorEntity):
    @property
    def native_value(self) -> StateType: ...
    @property
    def state_class(self) -> Union[str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...

class RpcSensor(ShellyRpcAttributeEntity, SensorEntity):
    @property
    def native_value(self) -> StateType: ...
    @property
    def state_class(self) -> Union[str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...

class BlockSleepingSensor(ShellySleepingBlockAttributeEntity, SensorEntity):
    @property
    def native_value(self) -> StateType: ...
    @property
    def state_class(self) -> Union[str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
