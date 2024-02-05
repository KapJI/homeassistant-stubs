from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, get_entry_data as get_entry_data
from .entity import BlockEntityDescription as BlockEntityDescription, ShellyBlockAttributeEntity as ShellyBlockAttributeEntity, async_setup_block_attribute_entities as async_setup_block_attribute_entities
from .utils import get_device_entry_gen as get_device_entry_gen
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from dataclasses import dataclass
from homeassistant.components.valve import ValveDeviceClass as ValveDeviceClass, ValveEntity as ValveEntity, ValveEntityDescription as ValveEntityDescription, ValveEntityFeature as ValveEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(kw_only=True, frozen=True)
class BlockValveDescription(BlockEntityDescription, ValveEntityDescription):
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, reports_position, icon_fn, unit_fn, value, available, removal_condition, extra_state_attributes) -> None: ...

GAS_VALVE: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def async_setup_block_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockShellyValve(ShellyBlockAttributeEntity, ValveEntity):
    entity_description: BlockValveDescription
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    control_result: Incomplete
    _attr_is_closed: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block, attribute: str, description: BlockValveDescription) -> None: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    async def async_open_valve(self, **kwargs: Any) -> None: ...
    async def async_close_valve(self, **kwargs: Any) -> None: ...
    def _update_callback(self) -> None: ...
