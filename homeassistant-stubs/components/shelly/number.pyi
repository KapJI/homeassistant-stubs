from .const import AIOSHELLY_DEVICE_TIMEOUT_SEC as AIOSHELLY_DEVICE_TIMEOUT_SEC, CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD
from .entity import BlockEntityDescription as BlockEntityDescription, ShellySleepingBlockAttributeEntity as ShellySleepingBlockAttributeEntity, async_setup_entry_attribute_entities as async_setup_entry_attribute_entities
from .utils import get_device_entry_gen as get_device_entry_gen
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from typing import Any, Final

_LOGGER: Final[Any]

class BlockNumberDescription(BlockEntityDescription, NumberEntityDescription):
    mode: NumberMode
    rest_path: str
    rest_arg: str
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, max_value, min_value, step, icon_fn, unit_fn, value, available, removal_condition, extra_state_attributes, mode, rest_path, rest_arg) -> None: ...

NUMBERS: Final[Any]

def _build_block_description(entry: RegistryEntry) -> BlockNumberDescription: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BlockSleepingNumber(ShellySleepingBlockAttributeEntity, NumberEntity):
    entity_description: BlockNumberDescription
    @property
    def value(self) -> float: ...
    async def async_set_value(self, value: float) -> None: ...
    async def _set_state_full_path(self, path: str, params: Any) -> Any: ...
