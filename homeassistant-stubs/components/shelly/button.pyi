from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DOMAIN as DOMAIN, MODEL_FRANKEVER_WATER_VALVE as MODEL_FRANKEVER_WATER_VALVE, ROLE_GENERIC as ROLE_GENERIC, SHELLY_GAS_MODELS as SHELLY_GAS_MODELS, SHELLY_WALL_DISPLAY_MODELS as SHELLY_WALL_DISPLAY_MODELS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import RpcEntityDescription as RpcEntityDescription, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingRpcAttributeEntity as ShellySleepingRpcAttributeEntity, async_setup_entry_rpc as async_setup_entry_rpc, get_entity_block_device_info as get_entity_block_device_info, get_entity_rpc_device_info as get_entity_rpc_device_info, rpc_call as rpc_call
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, async_remove_shelly_entity as async_remove_shelly_entity, format_ble_addr as format_ble_addr, get_blu_trv_device_info as get_blu_trv_device_info, get_device_entry_gen as get_device_entry_gen, get_rpc_key_id as get_rpc_key_id, get_virtual_component_ids as get_virtual_component_ids
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ShellyButtonDescription[_ShellyCoordinatorT: ShellyBlockCoordinator | ShellyRpcCoordinator](ButtonEntityDescription):
    press_action: str
    params: dict[str, Any] | None = ...
    supported: Callable[[_ShellyCoordinatorT], bool] = ...

@dataclass(frozen=True, kw_only=True)
class RpcButtonDescription(RpcEntityDescription, ButtonEntityDescription): ...

BUTTONS: Final[list[ShellyButtonDescription[Any]]]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ShellyBaseButton(CoordinatorEntity[ShellyRpcCoordinator | ShellyBlockCoordinator], ButtonEntity):
    _attr_has_entity_name: bool
    entity_description: ShellyButtonDescription[ShellyRpcCoordinator | ShellyBlockCoordinator]
    def __init__(self, coordinator: ShellyRpcCoordinator | ShellyBlockCoordinator, description: ShellyButtonDescription[ShellyRpcCoordinator | ShellyBlockCoordinator]) -> None: ...
    @override
    async def async_press(self) -> None: ...
    async def _press_method(self) -> None: ...

class ShellyButton(ShellyBaseButton):
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator | ShellyBlockCoordinator, description: ShellyButtonDescription[ShellyRpcCoordinator | ShellyBlockCoordinator]) -> None: ...
    @override
    async def _press_method(self) -> None: ...

class ShellyBluTrvButton(ShellyRpcAttributeEntity, ButtonEntity):
    entity_description: RpcButtonDescription
    _id: int
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcButtonDescription) -> None: ...
    @rpc_call
    @override
    async def async_press(self) -> None: ...

class RpcVirtualButton(ShellyRpcAttributeEntity, ButtonEntity):
    entity_description: RpcButtonDescription
    _id: int
    @rpc_call
    @override
    async def async_press(self) -> None: ...

class RpcSleepingSmokeMuteButton(ShellySleepingRpcAttributeEntity, ButtonEntity):
    entity_description: RpcButtonDescription
    @rpc_call
    @override
    async def async_press(self) -> None: ...
    @property
    @override
    def available(self) -> bool: ...

RPC_BUTTONS: Incomplete
