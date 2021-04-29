from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from collections.abc import Iterable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_ICON as ATTR_ICON, ATTR_RESTORED as ATTR_RESTORED, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.helpers.device_registry import EVENT_DEVICE_REGISTRY_UPDATED as EVENT_DEVICE_REGISTRY_UPDATED
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import slugify as slugify
from homeassistant.util.yaml import load_yaml as load_yaml
from typing import Any, Callable

PATH_REGISTRY: str
DATA_REGISTRY: str
EVENT_ENTITY_REGISTRY_UPDATED: str
SAVE_DELAY: int
_LOGGER: Any
DISABLED_CONFIG_ENTRY: str
DISABLED_DEVICE: str
DISABLED_HASS: str
DISABLED_INTEGRATION: str
DISABLED_USER: str
STORAGE_VERSION: int
STORAGE_KEY: str
ENTITY_DESCRIBING_ATTRIBUTES: Any

class RegistryEntry:
    entity_id: str = ...
    unique_id: str = ...
    platform: str = ...
    name: Union[str, None] = ...
    icon: Union[str, None] = ...
    device_id: Union[str, None] = ...
    area_id: Union[str, None] = ...
    config_entry_id: Union[str, None] = ...
    disabled_by: Union[str, None] = ...
    capabilities: Union[dict[str, Any], None] = ...
    supported_features: int = ...
    device_class: Union[str, None] = ...
    unit_of_measurement: Union[str, None] = ...
    original_name: Union[str, None] = ...
    original_icon: Union[str, None] = ...
    domain: str = ...
    def _domain_default(self) -> str: ...
    @property
    def disabled(self) -> bool: ...
    def write_unavailable_state(self, hass: HomeAssistant) -> None: ...
    def __init__(self, entity_id: Any, unique_id: Any, platform: Any, name: Any, icon: Any, device_id: Any, area_id: Any, config_entry_id: Any, disabled_by: Any, capabilities: Any, supported_features: Any, device_class: Any, unit_of_measurement: Any, original_name: Any, original_icon: Any, domain: Any) -> None: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...

class EntityRegistry:
    hass: Any = ...
    entities: Any
    _index: Any = ...
    _store: Any = ...
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_get_device_class_lookup(self, domain_device_classes: set) -> dict: ...
    def async_is_registered(self, entity_id: str) -> bool: ...
    def async_get(self, entity_id: str) -> Union[RegistryEntry, None]: ...
    def async_get_entity_id(self, domain: str, platform: str, unique_id: str) -> Union[str, None]: ...
    def async_generate_entity_id(self, domain: str, suggested_object_id: str, known_object_ids: Union[Iterable[str], None]=...) -> str: ...
    def async_get_or_create(self, domain: str, platform: str, unique_id: str, *, suggested_object_id: Union[str, None]=..., known_object_ids: Union[Iterable[str], None]=..., disabled_by: Union[str, None]=..., config_entry: Union[ConfigEntry, None]=..., device_id: Union[str, None]=..., area_id: Union[str, None]=..., capabilities: Union[dict[str, Any], None]=..., supported_features: Union[int, None]=..., device_class: Union[str, None]=..., unit_of_measurement: Union[str, None]=..., original_name: Union[str, None]=..., original_icon: Union[str, None]=...) -> RegistryEntry: ...
    def async_remove(self, entity_id: str) -> None: ...
    def async_device_modified(self, event: Event) -> None: ...
    def async_update_entity(self, entity_id: str, *, name: Union[str, None, UndefinedType]=..., icon: Union[str, None, UndefinedType]=..., area_id: Union[str, None, UndefinedType]=..., new_entity_id: Union[str, UndefinedType]=..., new_unique_id: Union[str, UndefinedType]=..., disabled_by: Union[str, None, UndefinedType]=...) -> RegistryEntry: ...
    def _async_update_entity(self, entity_id: str, *, name: Union[str, None, UndefinedType]=..., icon: Union[str, None, UndefinedType]=..., config_entry_id: Union[str, None, UndefinedType]=..., new_entity_id: Union[str, UndefinedType]=..., device_id: Union[str, None, UndefinedType]=..., area_id: Union[str, None, UndefinedType]=..., new_unique_id: Union[str, UndefinedType]=..., disabled_by: Union[str, None, UndefinedType]=..., capabilities: Union[dict[str, Any], None, UndefinedType]=..., supported_features: Union[int, UndefinedType]=..., device_class: Union[str, None, UndefinedType]=..., unit_of_measurement: Union[str, None, UndefinedType]=..., original_name: Union[str, None, UndefinedType]=..., original_icon: Union[str, None, UndefinedType]=...) -> RegistryEntry: ...
    async def async_load(self) -> None: ...
    def async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict[str, Any]: ...
    def async_clear_config_entry(self, config_entry: str) -> None: ...
    def async_clear_area_id(self, area_id: str) -> None: ...
    def _register_entry(self, entry: RegistryEntry) -> None: ...
    def _add_index(self, entry: RegistryEntry) -> None: ...
    def _unregister_entry(self, entry: RegistryEntry) -> None: ...
    def _remove_index(self, entry: RegistryEntry) -> None: ...
    def _rebuild_index(self) -> None: ...

def async_get(hass: HomeAssistant) -> EntityRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
async def async_get_registry(hass: HomeAssistant) -> EntityRegistry: ...
def async_entries_for_device(registry: EntityRegistry, device_id: str, include_disabled_entities: bool=...) -> list[RegistryEntry]: ...
def async_entries_for_area(registry: EntityRegistry, area_id: str) -> list[RegistryEntry]: ...
def async_entries_for_config_entry(registry: EntityRegistry, config_entry_id: str) -> list[RegistryEntry]: ...
def async_config_entry_disabled_by_changed(registry: EntityRegistry, config_entry: ConfigEntry) -> None: ...
async def _async_migrate(entities: dict[str, Any]) -> dict[str, list[dict[str, Any]]]: ...
def async_setup_entity_restore(hass: HomeAssistant, registry: EntityRegistry) -> None: ...
async def async_migrate_entries(hass: HomeAssistant, config_entry_id: str, entry_callback: Callable[[RegistryEntry], Union[dict, None]]) -> None: ...
