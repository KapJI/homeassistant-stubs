from . import BlockDeviceWrapper as BlockDeviceWrapper
from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, SHAIR_MAX_WORK_HOURS as SHAIR_MAX_WORK_HOURS
from .entity import BlockEntityDescription as BlockEntityDescription, RestEntityDescription as RestEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rest as async_setup_entry_rest, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import get_device_entry_gen as get_device_entry_gen, get_device_uptime as get_device_uptime, temperature_unit as temperature_unit
from aioshelly.block_device import Block as Block
from collections.abc import Mapping
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, DEGREE as DEGREE, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, Final

class BlockSensorDescription(BlockEntityDescription, SensorEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, icon_fn, unit_fn, value, available, removal_condition, extra_state_attributes) -> None: ...

class RpcSensorDescription(RpcEntityDescription, SensorEntityDescription):
    def __init__(self, sub_key, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, value, available, removal_condition, extra_state_attributes, use_polling_wrapper, supported) -> None: ...

class RestSensorDescription(RestEntityDescription, SensorEntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, value, extra_state_attributes) -> None: ...

SENSORS: Final[Any]
REST_SENSORS: Final[Any]
RPC_SENSORS: Final[Any]

def _build_block_description(entry: RegistryEntry) -> BlockSensorDescription: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockSensor(ShellyBlockAttributeEntity, SensorEntity):
    entity_description: BlockSensorDescription
    _attr_native_unit_of_measurement: Any
    def __init__(self, wrapper: BlockDeviceWrapper, block: Block, attribute: str, description: BlockSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class RestSensor(ShellyRestAttributeEntity, SensorEntity):
    entity_description: RestSensorDescription
    @property
    def native_value(self) -> StateType: ...

class RpcSensor(ShellyRpcAttributeEntity, SensorEntity):
    entity_description: RpcSensorDescription
    @property
    def native_value(self) -> StateType: ...

class BlockSleepingSensor(ShellySleepingBlockAttributeEntity, SensorEntity):
    entity_description: BlockSensorDescription
    _attr_native_unit_of_measurement: Any
    def __init__(self, wrapper: BlockDeviceWrapper, block: Union[Block, None], attribute: str, description: BlockSensorDescription, entry: Union[RegistryEntry, None] = ..., sensors: Union[Mapping[tuple[str, str], BlockSensorDescription], None] = ...) -> None: ...
    @property
    def native_value(self) -> StateType: ...
