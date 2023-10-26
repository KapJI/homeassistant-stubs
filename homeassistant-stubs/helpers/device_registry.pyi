from . import entity_registry as entity_registry, storage as storage
from .debounce import Debouncer as Debouncer
from .frame import report as report
from .json import JSON_DUMP as JSON_DUMP, find_paths_unserializable_data as find_paths_unserializable_data
from .typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from _typeshed import Incomplete
from collections import UserDict
from collections.abc import ValuesView
from enum import StrEnum
from homeassistant.backports.functools import cached_property as cached_property
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.json import format_unserializable_data as format_unserializable_data
from typing import Any, Literal, TypeVar, TypedDict
from yarl import URL

_LOGGER: Incomplete
DATA_REGISTRY: str
EVENT_DEVICE_REGISTRY_UPDATED: str
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int
SAVE_DELAY: int
CLEANUP_DELAY: int
CONNECTION_BLUETOOTH: str
CONNECTION_NETWORK_MAC: str
CONNECTION_UPNP: str
CONNECTION_ZIGBEE: str
ORPHANED_DEVICE_KEEP_SECONDS: Incomplete
RUNTIME_ONLY_ATTRS: Incomplete
CONFIGURATION_URL_SCHEMES: Incomplete

class DeviceEntryDisabler(StrEnum):
    CONFIG_ENTRY: str
    INTEGRATION: str
    USER: str

DISABLED_CONFIG_ENTRY: Incomplete
DISABLED_INTEGRATION: Incomplete
DISABLED_USER: Incomplete

class DeviceInfo(TypedDict, total=False):
    configuration_url: str | URL | None
    connections: set[tuple[str, str]]
    default_manufacturer: str
    default_model: str
    default_name: str
    entry_type: DeviceEntryType | None
    identifiers: set[tuple[str, str]]
    manufacturer: str | None
    model: str | None
    name: str | None
    serial_number: str | None
    suggested_area: str | None
    sw_version: str | None
    hw_version: str | None
    via_device: tuple[str, str]

DEVICE_INFO_TYPES: Incomplete
DEVICE_INFO_KEYS: Incomplete

class _EventDeviceRegistryUpdatedData_CreateRemove(TypedDict):
    action: Literal['create', 'remove']
    device_id: str

class _EventDeviceRegistryUpdatedData_Update(TypedDict):
    action: Literal['update']
    device_id: str
    changes: dict[str, Any]

EventDeviceRegistryUpdatedData: Incomplete

class DeviceEntryType(StrEnum):
    SERVICE: str

class DeviceInfoError(HomeAssistantError):
    device_info: Incomplete
    domain: Incomplete
    def __init__(self, domain: str, device_info: DeviceInfo, message: str) -> None: ...

def _validate_device_info(config_entry: ConfigEntry, device_info: DeviceInfo) -> str: ...
def _validate_configuration_url(value: Any) -> str | None: ...

class DeviceEntry:
    area_id: str | None
    config_entries: set[str]
    configuration_url: str | None
    connections: set[tuple[str, str]]
    disabled_by: DeviceEntryDisabler | None
    entry_type: DeviceEntryType | None
    hw_version: str | None
    id: str
    identifiers: set[tuple[str, str]]
    manufacturer: str | None
    model: str | None
    name_by_user: str | None
    name: str | None
    serial_number: str | None
    suggested_area: str | None
    sw_version: str | None
    via_device_id: str | None
    is_new: bool
    @property
    def disabled(self) -> bool: ...
    @property
    def dict_repr(self) -> dict[str, Any]: ...
    def json_repr(self) -> str | None: ...
    def __init__(self, area_id, config_entries, configuration_url, connections, disabled_by, entry_type, hw_version, id, identifiers, manufacturer, model, name_by_user, name, serial_number, suggested_area, sw_version, via_device_id, is_new) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class DeletedDeviceEntry:
    config_entries: set[str]
    connections: set[tuple[str, str]]
    identifiers: set[tuple[str, str]]
    id: str
    orphaned_timestamp: float | None
    def to_device_entry(self, config_entry_id: str, connections: set[tuple[str, str]], identifiers: set[tuple[str, str]]) -> DeviceEntry: ...
    def __init__(self, config_entries, connections, identifiers, id, orphaned_timestamp) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

def format_mac(mac: str) -> str: ...

class DeviceRegistryStore(storage.Store[dict[str, list[dict[str, Any]]]]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, list[dict[str, Any]]]) -> dict[str, Any]: ...
_EntryTypeT = TypeVar('_EntryTypeT', DeviceEntry, DeletedDeviceEntry)

class DeviceRegistryItems(UserDict[str, _EntryTypeT]):
    _connections: Incomplete
    _identifiers: Incomplete
    def __init__(self) -> None: ...
    def values(self) -> ValuesView[_EntryTypeT]: ...
    def __setitem__(self, key: str, entry: _EntryTypeT) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def get_entry(self, identifiers: set[tuple[str, str]] | None, connections: set[tuple[str, str]] | None) -> _EntryTypeT | None: ...

class DeviceRegistry:
    devices: DeviceRegistryItems[DeviceEntry]
    deleted_devices: DeviceRegistryItems[DeletedDeviceEntry]
    _device_data: dict[str, DeviceEntry]
    hass: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_get(self, device_id: str) -> DeviceEntry | None: ...
    def async_get_device(self, identifiers: set[tuple[str, str]] | None = ..., connections: set[tuple[str, str]] | None = ...) -> DeviceEntry | None: ...
    def _async_get_deleted_device(self, identifiers: set[tuple[str, str]], connections: set[tuple[str, str]]) -> DeletedDeviceEntry | None: ...
    def async_get_or_create(self, *, config_entry_id: str, configuration_url: str | URL | None | UndefinedType = ..., connections: set[tuple[str, str]] | None | UndefinedType = ..., default_manufacturer: str | None | UndefinedType = ..., default_model: str | None | UndefinedType = ..., default_name: str | None | UndefinedType = ..., disabled_by: DeviceEntryDisabler | None | UndefinedType = ..., entry_type: DeviceEntryType | None | UndefinedType = ..., hw_version: str | None | UndefinedType = ..., identifiers: set[tuple[str, str]] | None | UndefinedType = ..., manufacturer: str | None | UndefinedType = ..., model: str | None | UndefinedType = ..., name: str | None | UndefinedType = ..., serial_number: str | None | UndefinedType = ..., suggested_area: str | None | UndefinedType = ..., sw_version: str | None | UndefinedType = ..., via_device: tuple[str, str] | None | UndefinedType = ...) -> DeviceEntry: ...
    def async_update_device(self, device_id: str, *, add_config_entry_id: str | UndefinedType = ..., area_id: str | None | UndefinedType = ..., configuration_url: str | URL | None | UndefinedType = ..., disabled_by: DeviceEntryDisabler | None | UndefinedType = ..., entry_type: DeviceEntryType | None | UndefinedType = ..., hw_version: str | None | UndefinedType = ..., manufacturer: str | None | UndefinedType = ..., merge_connections: set[tuple[str, str]] | UndefinedType = ..., merge_identifiers: set[tuple[str, str]] | UndefinedType = ..., model: str | None | UndefinedType = ..., name_by_user: str | None | UndefinedType = ..., name: str | None | UndefinedType = ..., new_identifiers: set[tuple[str, str]] | UndefinedType = ..., remove_config_entry_id: str | UndefinedType = ..., serial_number: str | None | UndefinedType = ..., suggested_area: str | None | UndefinedType = ..., sw_version: str | None | UndefinedType = ..., via_device_id: str | None | UndefinedType = ...) -> DeviceEntry | None: ...
    def async_remove_device(self, device_id: str) -> None: ...
    async def async_load(self) -> None: ...
    def async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict[str, list[dict[str, Any]]]: ...
    def async_clear_config_entry(self, config_entry_id: str) -> None: ...
    def async_purge_expired_orphaned_devices(self) -> None: ...
    def async_clear_area_id(self, area_id: str) -> None: ...

def async_get(hass: HomeAssistant) -> DeviceRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
def async_entries_for_area(registry: DeviceRegistry, area_id: str) -> list[DeviceEntry]: ...
def async_entries_for_config_entry(registry: DeviceRegistry, config_entry_id: str) -> list[DeviceEntry]: ...
def async_config_entry_disabled_by_changed(registry: DeviceRegistry, config_entry: ConfigEntry) -> None: ...
def async_cleanup(hass: HomeAssistant, dev_reg: DeviceRegistry, ent_reg: entity_registry.EntityRegistry) -> None: ...
def async_setup_cleanup(hass: HomeAssistant, dev_reg: DeviceRegistry) -> None: ...
def _normalize_connections(connections: set[tuple[str, str]]) -> set[tuple[str, str]]: ...
