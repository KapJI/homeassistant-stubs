from .entity import BlockAttributeDescription as BlockAttributeDescription, RestAttributeDescription as RestAttributeDescription, RpcAttributeDescription as RpcAttributeDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rest as async_setup_entry_rest, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import get_device_entry_gen as get_device_entry_gen, is_block_momentary_input as is_block_momentary_input, is_rpc_momentary_input as is_rpc_momentary_input
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_CONNECTIVITY as DEVICE_CLASS_CONNECTIVITY, DEVICE_CLASS_GAS as DEVICE_CLASS_GAS, DEVICE_CLASS_MOISTURE as DEVICE_CLASS_MOISTURE, DEVICE_CLASS_MOTION as DEVICE_CLASS_MOTION, DEVICE_CLASS_OPENING as DEVICE_CLASS_OPENING, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_PROBLEM as DEVICE_CLASS_PROBLEM, DEVICE_CLASS_SMOKE as DEVICE_CLASS_SMOKE, DEVICE_CLASS_UPDATE as DEVICE_CLASS_UPDATE, DEVICE_CLASS_VIBRATION as DEVICE_CLASS_VIBRATION, STATE_ON as STATE_ON
from homeassistant.components.shelly.const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

SENSORS: Final[Any]
REST_SENSORS: Final[Any]
RPC_SENSORS: Final[Any]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockBinarySensor(ShellyBlockAttributeEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...

class RestBinarySensor(ShellyRestAttributeEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...

class RpcBinarySensor(ShellyRpcAttributeEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...

class BlockSleepingBinarySensor(ShellySleepingBlockAttributeEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
