from .const import DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .helpers import get_device_id as get_device_id, get_unique_id as get_unique_id
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.entity_registry import EntityRegistry as EntityRegistry, RegistryEntry as RegistryEntry, async_entries_for_device as async_entries_for_device
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.helpers.storage import Store as Store
from typing import Any, TypedDict
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.model.value import Value as ZwaveValue

_LOGGER: Any
LEGACY_ZWAVE_MIGRATION: Any
MIGRATED: str
STORAGE_WRITE_DELAY: int
STORAGE_KEY: Any
STORAGE_VERSION: int
NOTIFICATION_CC_LABEL_TO_PROPERTY_NAME: Any
SENSOR_MULTILEVEL_CC_LABEL_TO_PROPERTY_NAME: Any
CC_ID_LABEL_TO_PROPERTY: Any

class ZWaveMigrationData(TypedDict):
    node_id: int
    node_instance: int
    command_class: int
    command_class_label: str
    value_index: int
    device_id: str
    domain: str
    entity_id: str
    unique_id: str
    unit_of_measurement: Union[str, None]

class ZWaveJSMigrationData(TypedDict):
    node_id: int
    endpoint_index: int
    command_class: int
    value_property_name: str
    value_property_key_name: Union[str, None]
    value_id: str
    device_id: str
    domain: str
    entity_id: str
    unique_id: str
    unit_of_measurement: Union[str, None]

class LegacyZWaveMappedData:
    entity_entries: dict[str, ZWaveMigrationData]
    device_entries: dict[str, str]

async def async_add_migration_entity_value(hass: HomeAssistant, config_entry: ConfigEntry, entity_id: str, discovery_info: ZwaveDiscoveryInfo) -> None: ...
async def async_get_migration_data(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, ZWaveJSMigrationData]: ...
async def get_legacy_zwave_migration(hass: HomeAssistant) -> LegacyZWaveMigration: ...

class LegacyZWaveMigration:
    _hass: Any
    _store: Any
    _data: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def load_data(self) -> None: ...
    def save_data(self, config_entry_id: str, entity_id: str, data: ZWaveJSMigrationData) -> None: ...
    def _data_to_save(self) -> dict[str, dict[str, ZWaveJSMigrationData]]: ...
    def add_entity_value(self, config_entry: ConfigEntry, entity_id: str, discovery_info: ZwaveDiscoveryInfo) -> None: ...
    async def get_data(self, config_entry: ConfigEntry) -> dict[str, ZWaveJSMigrationData]: ...

def async_map_legacy_zwave_values(zwave_data: dict[str, ZWaveMigrationData], zwave_js_data: dict[str, ZWaveJSMigrationData]) -> LegacyZWaveMappedData: ...
async def async_migrate_legacy_zwave(hass: HomeAssistant, zwave_config_entry: ConfigEntry, zwave_js_config_entry: ConfigEntry, migration_map: LegacyZWaveMappedData) -> None: ...

class ValueID:
    command_class: str
    endpoint: str
    property_: str
    property_key: Union[str, None]
    @staticmethod
    def from_unique_id(unique_id: str) -> ValueID: ...
    @staticmethod
    def from_string_id(value_id_str: str) -> ValueID: ...
    def is_same_value_different_endpoints(self, other: ValueID) -> bool: ...

def async_migrate_old_entity(hass: HomeAssistant, ent_reg: EntityRegistry, registered_unique_ids: set[str], platform: str, device: DeviceEntry, unique_id: str) -> None: ...
def async_migrate_unique_id(ent_reg: EntityRegistry, platform: str, old_unique_id: str, new_unique_id: str) -> None: ...
def async_migrate_discovered_value(hass: HomeAssistant, ent_reg: EntityRegistry, registered_unique_ids: set[str], device: DeviceEntry, client: ZwaveClient, disc_info: ZwaveDiscoveryInfo) -> None: ...
def get_old_value_ids(value: ZwaveValue) -> list[str]: ...
