from . import BlockDeviceWrapper as BlockDeviceWrapper, RpcDeviceWrapper as RpcDeviceWrapper, RpcPollingWrapper as RpcPollingWrapper, ShellyDeviceRestWrapper as ShellyDeviceRestWrapper
from .const import AIOSHELLY_DEVICE_TIMEOUT_SEC as AIOSHELLY_DEVICE_TIMEOUT_SEC, BLOCK as BLOCK, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, REST as REST, RPC as RPC, RPC_POLL as RPC_POLL
from .utils import async_remove_shelly_entity as async_remove_shelly_entity, get_block_entity_name as get_block_entity_name, get_rpc_entity_name as get_rpc_entity_name, get_rpc_key_instances as get_rpc_key_instances
from aioshelly.block_device import Block as Block
from collections.abc import Callable as Callable, Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as device_registry, entity as entity, entity_registry as entity_registry, update_coordinator as update_coordinator
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, Final

_LOGGER: Final[Any]

async def async_setup_entry_attribute_entities(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, sensors: Mapping[tuple[str, str], BlockEntityDescription], sensor_class: Callable, description_class: Callable[[entity_registry.RegistryEntry], BlockEntityDescription]) -> None: ...
async def async_setup_block_attribute_entities(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, wrapper: BlockDeviceWrapper, sensors: Mapping[tuple[str, str], BlockEntityDescription], sensor_class: Callable) -> None: ...
async def async_restore_block_attribute_entities(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, wrapper: BlockDeviceWrapper, sensors: Mapping[tuple[str, str], BlockEntityDescription], sensor_class: Callable, description_class: Callable[[entity_registry.RegistryEntry], BlockEntityDescription]) -> None: ...
async def async_setup_entry_rpc(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, sensors: Mapping[str, RpcEntityDescription], sensor_class: Callable) -> None: ...
async def async_setup_entry_rest(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, sensors: Mapping[str, RestEntityDescription], sensor_class: Callable) -> None: ...

class BlockEntityDescription(EntityDescription):
    icon_fn: Union[Callable[[dict], str], None]
    unit_fn: Union[Callable[[dict], str], None]
    value: Callable[[Any], Any]
    available: Union[Callable[[Block], bool], None]
    removal_condition: Union[Callable[[dict, Block], bool], None]
    extra_state_attributes: Union[Callable[[Block], Union[dict, None]], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, icon_fn, unit_fn, value, available, removal_condition, extra_state_attributes) -> None: ...

class RpcEntityRequiredKeysMixin:
    sub_key: str
    def __init__(self, sub_key) -> None: ...

class RpcEntityDescription(EntityDescription, RpcEntityRequiredKeysMixin):
    value: Union[Callable[[Any, Any], Any], None]
    available: Union[Callable[[dict], bool], None]
    removal_condition: Union[Callable[[dict, str], bool], None]
    extra_state_attributes: Union[Callable[[dict, dict], Union[dict, None]], None]
    use_polling_wrapper: bool
    supported: Callable
    def __init__(self, sub_key, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, value, available, removal_condition, extra_state_attributes, use_polling_wrapper, supported) -> None: ...

class RestEntityDescription(EntityDescription):
    value: Union[Callable[[dict, Any], Any], None]
    extra_state_attributes: Union[Callable[[dict], Union[dict, None]], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, value, extra_state_attributes) -> None: ...

class ShellyBlockEntity(entity.Entity):
    wrapper: Any
    block: Any
    _attr_name: Any
    _attr_should_poll: bool
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, wrapper: BlockDeviceWrapper, block: Block) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    def _update_callback(self) -> None: ...
    async def set_state(self, **kwargs: Any) -> Any: ...

class ShellyRpcEntity(entity.Entity):
    wrapper: Any
    key: Any
    _attr_should_poll: bool
    _attr_device_info: Any
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, wrapper: Union[RpcDeviceWrapper, RpcPollingWrapper], key: str) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    def _update_callback(self) -> None: ...
    async def call_rpc(self, method: str, params: Any) -> Any: ...

class ShellyBlockAttributeEntity(ShellyBlockEntity, entity.Entity):
    entity_description: BlockEntityDescription
    attribute: Any
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, wrapper: BlockDeviceWrapper, block: Block, attribute: str, description: BlockEntityDescription) -> None: ...
    @property
    def attribute_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class ShellyRestAttributeEntity(update_coordinator.CoordinatorEntity):
    entity_description: RestEntityDescription
    wrapper: Any
    attribute: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    _last_value: Any
    def __init__(self, wrapper: BlockDeviceWrapper, attribute: str, description: RestEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def attribute_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class ShellyRpcAttributeEntity(ShellyRpcEntity, entity.Entity):
    entity_description: RpcEntityDescription
    attribute: Any
    _attr_unique_id: Any
    _attr_name: Any
    _last_value: Any
    def __init__(self, wrapper: RpcDeviceWrapper, key: str, attribute: str, description: RpcEntityDescription) -> None: ...
    @property
    def attribute_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class ShellySleepingBlockAttributeEntity(ShellyBlockAttributeEntity, RestoreEntity):
    sensors: Any
    last_state: Any
    wrapper: Any
    attribute: Any
    block: Any
    entity_description: Any
    _attr_should_poll: bool
    _attr_device_info: Any
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, wrapper: BlockDeviceWrapper, block: Union[Block, None], attribute: str, description: BlockEntityDescription, entry: Union[entity_registry.RegistryEntry, None] = ..., sensors: Union[Mapping[tuple[str, str], BlockEntityDescription], None] = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _update_callback(self) -> None: ...
