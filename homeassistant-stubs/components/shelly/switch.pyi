from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, MOTION_MODELS as MOTION_MODELS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import BlockEntityDescription as BlockEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyBlockEntity as ShellyBlockEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellyRpcEntity as ShellyRpcEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, async_remove_shelly_entity as async_remove_shelly_entity, get_device_entry_gen as get_device_entry_gen, get_rpc_key_ids as get_rpc_key_ids, get_virtual_component_ids as get_virtual_component_ids, is_block_channel_type_light as is_block_channel_type_light, is_rpc_channel_type_light as is_rpc_channel_type_light, is_rpc_thermostat_internal_actuator as is_rpc_thermostat_internal_actuator, is_rpc_thermostat_mode as is_rpc_thermostat_mode
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

@dataclass(frozen=True, kw_only=True)
class BlockSwitchDescription(BlockEntityDescription, SwitchEntityDescription): ...

MOTION_SWITCH: Incomplete

@dataclass(frozen=True, kw_only=True)
class RpcSwitchDescription(RpcEntityDescription, SwitchEntityDescription):
    is_on: Callable[[dict[str, Any]], bool]
    method_on: str
    method_off: str
    method_params_fn: Callable[[int | None, bool], dict]

RPC_SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def async_setup_block_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def async_setup_rpc_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BlockSleepingMotionSwitch(ShellySleepingBlockAttributeEntity, RestoreEntity, SwitchEntity):
    entity_description: BlockSwitchDescription
    _attr_translation_key: str
    last_state: State | None
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block | None, attribute: str, description: BlockSwitchDescription, entry: RegistryEntry | None = None) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class BlockRelaySwitch(ShellyBlockEntity, SwitchEntity):
    control_result: dict[str, Any] | None
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def _update_callback(self) -> None: ...

class RpcRelaySwitch(ShellyRpcEntity, SwitchEntity):
    _id: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, id_: int) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class RpcSwitch(ShellyRpcAttributeEntity, SwitchEntity):
    entity_description: RpcSwitchDescription
    _attr_has_entity_name: bool
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
