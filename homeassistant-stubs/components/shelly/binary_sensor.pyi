from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD
from .coordinator import ShellyConfigEntry as ShellyConfigEntry
from .entity import BlockEntityDescription as BlockEntityDescription, RestEntityDescription as RestEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, ShellySleepingRpcAttributeEntity as ShellySleepingRpcAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities, async_setup_entry_rest as async_setup_entry_rest, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import async_remove_orphaned_virtual_entities as async_remove_orphaned_virtual_entities, get_device_entry_gen as get_device_entry_gen, get_virtual_component_ids as get_virtual_component_ids, is_block_momentary_input as is_block_momentary_input, is_rpc_momentary_input as is_rpc_momentary_input
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Final

@dataclass(frozen=True, kw_only=True)
class BlockBinarySensorDescription(BlockEntityDescription, BinarySensorEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., unit_fn=..., value=..., available=..., removal_condition=..., extra_state_attributes=...) -> None: ...

@dataclass(frozen=True, kw_only=True)
class RpcBinarySensorDescription(RpcEntityDescription, BinarySensorEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., sub_key, value=..., available=..., removal_condition=..., extra_state_attributes=..., use_polling_coordinator=..., supported=..., unit=..., options_fn=...) -> None: ...

@dataclass(frozen=True, kw_only=True)
class RestBinarySensorDescription(RestEntityDescription, BinarySensorEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., value=..., extra_state_attributes=...) -> None: ...

SENSORS: dict[tuple[str, str], BlockBinarySensorDescription]
REST_SENSORS: Final[Incomplete]
RPC_SENSORS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockBinarySensor(ShellyBlockAttributeEntity, BinarySensorEntity):
    entity_description: BlockBinarySensorDescription
    @property
    def is_on(self) -> bool: ...

class RestBinarySensor(ShellyRestAttributeEntity, BinarySensorEntity):
    entity_description: RestBinarySensorDescription
    @property
    def is_on(self) -> bool: ...

class RpcBinarySensor(ShellyRpcAttributeEntity, BinarySensorEntity):
    entity_description: RpcBinarySensorDescription
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
    last_state: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
