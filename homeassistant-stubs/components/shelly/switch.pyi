from .const import MODEL_FRANKEVER_IRRIGATION_CONTROLLER as MODEL_FRANKEVER_IRRIGATION_CONTROLLER, MODEL_LINKEDGO_ST1820_THERMOSTAT as MODEL_LINKEDGO_ST1820_THERMOSTAT, MODEL_LINKEDGO_ST802_THERMOSTAT as MODEL_LINKEDGO_ST802_THERMOSTAT, MODEL_NEO_WATER_VALVE as MODEL_NEO_WATER_VALVE, MODEL_TOP_EV_CHARGER_EVE01 as MODEL_TOP_EV_CHARGER_EVE01, ROLE_GENERIC as ROLE_GENERIC
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import BlockEntityDescription as BlockEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rpc as async_setup_entry_rpc, rpc_call as rpc_call
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, get_device_entry_gen as get_device_entry_gen, get_rpc_channel_name as get_rpc_channel_name, get_virtual_component_ids as get_virtual_component_ids, is_block_exclude_from_relay as is_block_exclude_from_relay, is_rpc_exclude_from_relay as is_rpc_exclude_from_relay, is_view_for_platform as is_view_for_platform
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class BlockSwitchDescription(BlockEntityDescription, SwitchEntityDescription): ...

BLOCK_RELAY_SWITCHES: Incomplete
BLOCK_SLEEPING_MOTION_SWITCH: Incomplete

@dataclass(frozen=True, kw_only=True)
class RpcSwitchDescription(RpcEntityDescription, SwitchEntityDescription):
    is_on: Callable[[dict[str, Any]], bool]
    method_on: str
    method_off: str
    method_params_fn: Callable[[int | None, bool], tuple]

RPC_RELAY_SWITCHES: Incomplete
RPC_SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_block_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_rpc_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BlockSleepingMotionSwitch(ShellySleepingBlockAttributeEntity, RestoreEntity, SwitchEntity):
    entity_description: BlockSwitchDescription
    last_state: State | None
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block | None, attribute: str, description: BlockSwitchDescription, entry: RegistryEntry | None = None) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class BlockRelaySwitch(ShellyBlockAttributeEntity, SwitchEntity):
    entity_description: BlockSwitchDescription
    control_result: dict[str, Any] | None
    _attr_name: Incomplete
    _attr_unique_id: str
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block, attribute: str, description: BlockSwitchDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def _update_callback(self) -> None: ...

class RpcSwitch(ShellyRpcAttributeEntity, SwitchEntity):
    entity_description: RpcSwitchDescription
    _attr_name: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcSwitchDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @rpc_call
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @rpc_call
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class RpcRelaySwitch(RpcSwitch):
    _attr_unique_id: str
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcSwitchDescription) -> None: ...
