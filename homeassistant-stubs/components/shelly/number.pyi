from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, LOGGER as LOGGER
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator
from .entity import BlockEntityDescription as BlockEntityDescription, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities
from _typeshed import Incomplete
from aioshelly.block_device import Block as Block
from collections.abc import Mapping
from dataclasses import dataclass
from homeassistant.components.number import NumberEntityDescription as NumberEntityDescription, NumberExtraStoredData as NumberExtraStoredData, NumberMode as NumberMode, RestoreNumber as RestoreNumber
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from typing import Any, Final

@dataclass
class BlockNumberDescription(BlockEntityDescription, NumberEntityDescription):
    rest_path: str = ...
    rest_arg: str = ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step, icon_fn, unit_fn, value, available, removal_condition, extra_state_attributes, rest_path, rest_arg) -> None: ...

NUMBERS: Final[Incomplete]

def _build_block_description(entry: RegistryEntry) -> BlockNumberDescription: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockSleepingNumber(ShellySleepingBlockAttributeEntity, RestoreNumber):
    entity_description: BlockNumberDescription
    restored_data: Incomplete
    def __init__(self, coordinator: ShellyBlockCoordinator, block: Block | None, attribute: str, description: BlockNumberDescription, entry: RegistryEntry | None = ..., sensors: Mapping[tuple[str, str], BlockNumberDescription] | None = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    async def _set_state_full_path(self, path: str, params: Any) -> Any: ...
