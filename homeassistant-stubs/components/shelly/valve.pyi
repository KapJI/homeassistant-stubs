from .const import MODEL_FRANKEVER_IRRIGATION_CONTROLLER as MODEL_FRANKEVER_IRRIGATION_CONTROLLER, MODEL_FRANKEVER_WATER_VALVE as MODEL_FRANKEVER_WATER_VALVE, MODEL_NEO_WATER_VALVE as MODEL_NEO_WATER_VALVE
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import BlockEntityDescription as BlockEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, async_setup_block_attribute_entities as async_setup_block_attribute_entities, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import get_device_entry_gen as get_device_entry_gen
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from dataclasses import dataclass
from homeassistant.components.valve import ValveDeviceClass as ValveDeviceClass, ValveEntity as ValveEntity, ValveEntityDescription as ValveEntityDescription, ValveEntityFeature as ValveEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class BlockValveDescription(BlockEntityDescription, ValveEntityDescription): ...
@dataclass(kw_only=True, frozen=True)
class RpcValveDescription(RpcEntityDescription, ValveEntityDescription): ...

BLOCK_VALVES: dict[tuple[str, str], BlockValveDescription]

class RpcShellyBaseWaterValve(ShellyRpcAttributeEntity, ValveEntity):
    entity_description: RpcValveDescription
    _attr_device_class: Incomplete
    _id: int
    _attr_name: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcEntityDescription) -> None: ...

class RpcShellyWaterValve(RpcShellyBaseWaterValve):
    _attr_supported_features: Incomplete
    _attr_reports_position: bool
    @property
    def current_valve_position(self) -> int: ...
    async def async_set_valve_position(self, position: int) -> None: ...

class RpcShellySimpleWaterValve(RpcShellyBaseWaterValve):
    _attr_supported_features: Incomplete
    _attr_reports_position: bool
    @property
    def is_closed(self) -> bool | None: ...
    async def async_open_valve(self, **kwargs: Any) -> None: ...
    async def async_close_valve(self, **kwargs: Any) -> None: ...

RPC_VALVES: dict[str, RpcValveDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_block_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_rpc_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BlockShellyValve(ShellyBlockAttributeEntity, ValveEntity):
    entity_description: BlockValveDescription
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    control_result: dict[str, Any] | None
    _attr_is_closed: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block, attribute: str, description: BlockValveDescription) -> None: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    async def async_open_valve(self, **kwargs: Any) -> None: ...
    async def async_close_valve(self, **kwargs: Any) -> None: ...
    @callback
    def _update_callback(self) -> None: ...
