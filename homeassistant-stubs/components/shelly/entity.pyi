from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, LOGGER as LOGGER
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyRpcCoordinator as ShellyRpcCoordinator, get_entry_data as get_entry_data
from .utils import async_remove_shelly_entity as async_remove_shelly_entity, get_block_entity_name as get_block_entity_name, get_rpc_entity_name as get_rpc_entity_name, get_rpc_key_instances as get_rpc_key_instances
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from collections.abc import Callable as Callable, Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_entries_for_config_entry as async_entries_for_config_entry
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

def async_setup_entry_attribute_entities(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, sensors: Mapping[tuple[str, str], BlockEntityDescription], sensor_class: Callable, description_class: Callable[[RegistryEntry], BlockEntityDescription]) -> None: ...
def async_setup_block_attribute_entities(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, coordinator: ShellyBlockCoordinator, sensors: Mapping[tuple[str, str], BlockEntityDescription], sensor_class: Callable) -> None: ...
def async_restore_block_attribute_entities(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, coordinator: ShellyBlockCoordinator, sensors: Mapping[tuple[str, str], BlockEntityDescription], sensor_class: Callable, description_class: Callable[[RegistryEntry], BlockEntityDescription]) -> None: ...
def async_setup_entry_rpc(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, sensors: Mapping[str, RpcEntityDescription], sensor_class: Callable) -> None: ...
def async_setup_rpc_attribute_entities(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, sensors: Mapping[str, RpcEntityDescription], sensor_class: Callable) -> None: ...
def async_restore_rpc_attribute_entities(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, coordinator: ShellyRpcCoordinator, sensors: Mapping[str, RpcEntityDescription], sensor_class: Callable) -> None: ...
def async_setup_entry_rest(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, sensors: Mapping[str, RestEntityDescription], sensor_class: Callable) -> None: ...

class BlockEntityDescription(EntityDescription):
    icon_fn: Union[Callable[[dict], str], None]
    unit_fn: Union[Callable[[dict], str], None]
    value: Callable[[Any], Any]
    available: Union[Callable[[Block], bool], None]
    removal_condition: Union[Callable[[dict, Block], bool], None]
    extra_state_attributes: Union[Callable[[Block], Union[dict, None]], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, icon_fn, unit_fn, value, available, removal_condition, extra_state_attributes) -> None: ...

class RpcEntityRequiredKeysMixin:
    sub_key: str
    def __init__(self, sub_key) -> None: ...

class RpcEntityDescription(EntityDescription, RpcEntityRequiredKeysMixin):
    value: Union[Callable[[Any, Any], Any], None]
    available: Union[Callable[[dict], bool], None]
    removal_condition: Union[Callable[[dict, dict, str], bool], None]
    extra_state_attributes: Union[Callable[[dict, dict], Union[dict, None]], None]
    use_polling_coordinator: bool
    supported: Callable
    def __init__(self, sub_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, value, available, removal_condition, extra_state_attributes, use_polling_coordinator, supported) -> None: ...

class RestEntityDescription(EntityDescription):
    value: Union[Callable[[dict, Any], Any], None]
    extra_state_attributes: Union[Callable[[dict], Union[dict, None]], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, value, extra_state_attributes) -> None: ...

class ShellyBlockEntity(CoordinatorEntity[ShellyBlockCoordinator]):
    block: Incomplete
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    def _update_callback(self) -> None: ...
    async def set_state(self, **kwargs: Any) -> Any: ...

class ShellyRpcEntity(CoordinatorEntity[ShellyRpcCoordinator]):
    key: Incomplete
    _attr_should_poll: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def status(self) -> dict: ...
    async def async_added_to_hass(self) -> None: ...
    def _update_callback(self) -> None: ...
    async def call_rpc(self, method: str, params: Any) -> Any: ...

class ShellyBlockAttributeEntity(ShellyBlockEntity, Entity):
    entity_description: BlockEntityDescription
    attribute: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block, attribute: str, description: BlockEntityDescription) -> None: ...
    @property
    def attribute_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class ShellyRestAttributeEntity(CoordinatorEntity[ShellyBlockCoordinator]):
    entity_description: RestEntityDescription
    block_coordinator: Incomplete
    attribute: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _last_value: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, attribute: str, description: RestEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def attribute_value(self) -> StateType: ...

class ShellyRpcAttributeEntity(ShellyRpcEntity, Entity):
    entity_description: RpcEntityDescription
    attribute: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _last_value: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcEntityDescription) -> None: ...
    @property
    def sub_status(self) -> Any: ...
    @property
    def attribute_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...

class ShellySleepingBlockAttributeEntity(ShellyBlockAttributeEntity, RestoreEntity):
    sensors: Incomplete
    last_state: Incomplete
    last_unit: Incomplete
    coordinator: Incomplete
    attribute: Incomplete
    block: Incomplete
    entity_description: Incomplete
    _attr_should_poll: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Union[Block, None], attribute: str, description: BlockEntityDescription, entry: Union[RegistryEntry, None] = ..., sensors: Union[Mapping[tuple[str, str], BlockEntityDescription], None] = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _update_callback(self) -> None: ...

class ShellySleepingRpcAttributeEntity(ShellyRpcAttributeEntity, RestoreEntity):
    entity_description: RpcEntityDescription
    last_state: Incomplete
    last_unit: Incomplete
    coordinator: Incomplete
    key: Incomplete
    attribute: Incomplete
    _attr_should_poll: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _last_value: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcEntityDescription, entry: Union[RegistryEntry, None] = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
