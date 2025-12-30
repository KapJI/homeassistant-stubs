from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, MODEL_FRANKEVER_WATER_VALVE as MODEL_FRANKEVER_WATER_VALVE, ROLE_GENERIC as ROLE_GENERIC
from .coordinator import ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import BlockEntityDescription as BlockEntityDescription, RestEntityDescription as RestEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, ShellySleepingRpcAttributeEntity as ShellySleepingRpcAttributeEntity, async_setup_entry_block as async_setup_entry_block, async_setup_entry_rest as async_setup_entry_rest, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, get_blu_trv_device_info as get_blu_trv_device_info, get_device_entry_gen as get_device_entry_gen, get_rpc_custom_name as get_rpc_custom_name, get_rpc_key as get_rpc_key, is_block_momentary_input as is_block_momentary_input, is_rpc_momentary_input as is_rpc_momentary_input, is_view_for_platform as is_view_for_platform
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class BlockBinarySensorDescription(BlockEntityDescription, BinarySensorEntityDescription): ...
@dataclass(frozen=True, kw_only=True)
class RpcBinarySensorDescription(RpcEntityDescription, BinarySensorEntityDescription): ...
@dataclass(frozen=True, kw_only=True)
class RestBinarySensorDescription(RestEntityDescription, BinarySensorEntityDescription): ...

class RpcBinarySensor(ShellyRpcAttributeEntity, BinarySensorEntity):
    entity_description: RpcBinarySensorDescription
    _attr_name: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_translation_key: str
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...

class RpcPresenceBinarySensor(RpcBinarySensor):
    @property
    def available(self) -> bool: ...

class RpcBluTrvBinarySensor(RpcBinarySensor):
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcBinarySensorDescription) -> None: ...

BLOCK_SENSORS: dict[tuple[str, str], BlockBinarySensorDescription]
REST_SENSORS: Final[Incomplete]
RPC_SENSORS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_block_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def _async_setup_rpc_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BlockBinarySensor(ShellyBlockAttributeEntity, BinarySensorEntity):
    entity_description: BlockBinarySensorDescription
    @property
    def is_on(self) -> bool: ...

class RestBinarySensor(ShellyRestAttributeEntity, BinarySensorEntity):
    entity_description: RestBinarySensorDescription
    @property
    def is_on(self) -> bool: ...

class BlockSleepingBinarySensor(ShellySleepingBlockAttributeEntity, BinarySensorEntity, RestoreEntity):
    entity_description: BlockBinarySensorDescription
    last_state: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class RpcSleepingBinarySensor(ShellySleepingRpcAttributeEntity, BinarySensorEntity, RestoreEntity):
    entity_description: RpcBinarySensorDescription
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcBinarySensorDescription, entry: RegistryEntry | None = None) -> None: ...
    last_state: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
