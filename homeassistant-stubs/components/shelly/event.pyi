from .const import BASIC_INPUTS_EVENTS_TYPES as BASIC_INPUTS_EVENTS_TYPES, RPC_INPUTS_EVENTS_TYPES as RPC_INPUTS_EVENTS_TYPES, SHIX3_1_INPUTS_EVENTS_TYPES as SHIX3_1_INPUTS_EVENTS_TYPES
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import ShellyBlockEntity as ShellyBlockEntity, ShellyRpcEntity as ShellyRpcEntity
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, async_remove_shelly_entity as async_remove_shelly_entity, get_block_channel as get_block_channel, get_block_custom_name as get_block_custom_name, get_block_number_of_channels as get_block_number_of_channels, get_device_entry_gen as get_device_entry_gen, get_rpc_custom_name as get_rpc_custom_name, get_rpc_key as get_rpc_key, get_rpc_key_id as get_rpc_key_id, get_rpc_key_instances as get_rpc_key_instances, get_rpc_number_of_channels as get_rpc_number_of_channels, is_block_momentary_input as is_block_momentary_input, is_block_single_device as is_block_single_device, is_rpc_momentary_input as is_rpc_momentary_input
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.event import EventDeviceClass as EventDeviceClass, EventEntity as EventEntity, EventEntityDescription as EventEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ShellyBlockEventDescription(EventEntityDescription):
    removal_condition: Callable[[dict, Block], bool] | None = ...

@dataclass(frozen=True, kw_only=True)
class ShellyRpcEventDescription(EventEntityDescription):
    removal_condition: Callable[[dict, dict, str], bool] | None = ...

BLOCK_EVENT: Final[Incomplete]
RPC_EVENT: Final[Incomplete]
SCRIPT_EVENT: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_block_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_rpc_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ShellyBlockEvent(ShellyBlockEntity, EventEntity):
    entity_description: ShellyBlockEventDescription
    channel: Incomplete
    _attr_unique_id: Incomplete
    _attr_event_types: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block, description: ShellyBlockEventDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, event: dict[str, Any]) -> None: ...

class ShellyRpcEvent(ShellyRpcEntity, EventEntity):
    _attr_has_entity_name: bool
    entity_description: ShellyRpcEventDescription
    _attr_name: Incomplete
    _attr_translation_placeholders: Incomplete
    event_id: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, description: ShellyRpcEventDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, event: dict[str, Any]) -> None: ...

class ShellyRpcScriptEvent(ShellyRpcEntity, EventEntity):
    _attr_has_entity_name: bool
    entity_description: ShellyRpcEventDescription
    _attr_event_types: Incomplete
    _attr_name: Incomplete
    event_id: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, description: ShellyRpcEventDescription, event_types: list[str]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_handle_event(self, event: dict[str, Any]) -> None: ...
