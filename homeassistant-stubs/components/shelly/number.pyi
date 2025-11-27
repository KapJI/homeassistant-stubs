from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DOMAIN as DOMAIN, LOGGER as LOGGER, MODEL_FRANKEVER_WATER_VALVE as MODEL_FRANKEVER_WATER_VALVE, MODEL_LINKEDGO_ST1820_THERMOSTAT as MODEL_LINKEDGO_ST1820_THERMOSTAT, MODEL_LINKEDGO_ST802_THERMOSTAT as MODEL_LINKEDGO_ST802_THERMOSTAT, MODEL_TOP_EV_CHARGER_EVE01 as MODEL_TOP_EV_CHARGER_EVE01, ROLE_GENERIC as ROLE_GENERIC, VIRTUAL_NUMBER_MODE_MAP as VIRTUAL_NUMBER_MODE_MAP
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import BlockEntityDescription as BlockEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rpc as async_setup_entry_rpc, rpc_call as rpc_call
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, get_blu_trv_device_info as get_blu_trv_device_info, get_device_entry_gen as get_device_entry_gen, get_virtual_component_ids as get_virtual_component_ids, get_virtual_component_unit as get_virtual_component_unit, is_view_for_platform as is_view_for_platform
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberExtraStoredData as NumberExtraStoredData, NumberMode as NumberMode, RestoreNumber as RestoreNumber
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from typing import Any, Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class BlockNumberDescription(BlockEntityDescription, NumberEntityDescription):
    rest_path: str = ...
    rest_arg: str = ...

@dataclass(frozen=True, kw_only=True)
class RpcNumberDescription(RpcEntityDescription, NumberEntityDescription):
    max_fn: Callable[[dict], float] | None = ...
    min_fn: Callable[[dict], float] | None = ...
    step_fn: Callable[[dict], float] | None = ...
    mode_fn: Callable[[dict], NumberMode] | None = ...
    slot: str | None = ...
    method: str

class RpcNumber(ShellyRpcAttributeEntity, NumberEntity):
    entity_description: RpcNumberDescription
    attribute_value: float | None
    _id: int | None
    _attr_native_max_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_step: Incomplete
    _attr_mode: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcNumberDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    @rpc_call
    async def async_set_native_value(self, value: float) -> None: ...

class RpcCuryIntensityNumber(RpcNumber):
    @rpc_call
    async def async_set_native_value(self, value: float) -> None: ...

class RpcBluTrvNumber(RpcNumber):
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcNumberDescription) -> None: ...

class RpcBluTrvExtTempNumber(RpcBluTrvNumber):
    _reported_value: float | None
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...

NUMBERS: dict[tuple[str, str], BlockNumberDescription]
RPC_NUMBERS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_block_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_rpc_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BlockSleepingNumber(ShellySleepingBlockAttributeEntity, RestoreNumber):
    entity_description: BlockNumberDescription
    restored_data: NumberExtraStoredData | None
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block | None, attribute: str, description: BlockNumberDescription, entry: RegistryEntry | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    async def _set_state_full_path(self, path: str, params: Any) -> Any: ...
