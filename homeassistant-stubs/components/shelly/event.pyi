from .const import BASIC_INPUTS_EVENTS_TYPES as BASIC_INPUTS_EVENTS_TYPES, RPC_INPUTS_EVENTS_TYPES as RPC_INPUTS_EVENTS_TYPES, SHIX3_1_INPUTS_EVENTS_TYPES as SHIX3_1_INPUTS_EVENTS_TYPES
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyRpcCoordinator as ShellyRpcCoordinator, get_entry_data as get_entry_data
from .entity import ShellyBlockEntity as ShellyBlockEntity
from .utils import async_remove_shelly_entity as async_remove_shelly_entity, get_device_entry_gen as get_device_entry_gen, get_rpc_entity_name as get_rpc_entity_name, get_rpc_key_instances as get_rpc_key_instances, is_block_momentary_input as is_block_momentary_input, is_rpc_momentary_input as is_rpc_momentary_input
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from collections.abc import Callable as Callable
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

class ShellyBlockEventDescription(EventEntityDescription):
    removal_condition: Callable[[dict, Block], bool] | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, event_types, removal_condition) -> None: ...

class ShellyRpcEventDescription(EventEntityDescription):
    removal_condition: Callable[[dict, dict, str], bool] | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, event_types, removal_condition) -> None: ...

BLOCK_EVENT: Final[Incomplete]
RPC_EVENT: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ShellyBlockEvent(ShellyBlockEntity, EventEntity):
    entity_description: ShellyBlockEventDescription
    channel: Incomplete
    _attr_unique_id: Incomplete
    _attr_event_types: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block, description: ShellyBlockEventDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_handle_event(self, event: dict[str, Any]) -> None: ...

class ShellyRpcEvent(CoordinatorEntity[ShellyRpcCoordinator], EventEntity):
    entity_description: ShellyRpcEventDescription
    input_index: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, description: ShellyRpcEventDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_handle_event(self, event: dict[str, Any]) -> None: ...
