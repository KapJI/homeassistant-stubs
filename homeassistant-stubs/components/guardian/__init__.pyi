import asyncio
from .const import API_SENSOR_PAIRED_SENSOR_STATUS as API_SENSOR_PAIRED_SENSOR_STATUS, API_SENSOR_PAIR_DUMP as API_SENSOR_PAIR_DUMP, API_SYSTEM_DIAGNOSTICS as API_SYSTEM_DIAGNOSTICS, API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, API_VALVE_STATUS as API_VALVE_STATUS, API_WIFI_STATUS as API_WIFI_STATUS, CONF_UID as CONF_UID, DOMAIN as DOMAIN, LOGGER as LOGGER, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from .util import GuardianDataUpdateCoordinator as GuardianDataUpdateCoordinator
from _typeshed import Incomplete
from aioguardian import Client
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_FILENAME as CONF_FILENAME, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PORT as CONF_PORT, CONF_URL as CONF_URL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

DATA_PAIRED_SENSOR_MANAGER: str
SERVICE_NAME_PAIR_SENSOR: str
SERVICE_NAME_UNPAIR_SENSOR: str
SERVICE_NAME_UPGRADE_FIRMWARE: str
SERVICES: Incomplete
SERVICE_BASE_SCHEMA: Incomplete
SERVICE_PAIR_UNPAIR_SENSOR_SCHEMA: Incomplete
SERVICE_UPGRADE_FIRMWARE_SCHEMA: Incomplete
PLATFORMS: Incomplete

@dataclass
class GuardianData:
    entry: ConfigEntry
    client: Client
    valve_controller_coordinators: dict[str, GuardianDataUpdateCoordinator]
    paired_sensor_manager: PairedSensorManager
    def __init__(self, entry, client, valve_controller_coordinators, paired_sensor_manager) -> None: ...

def async_get_entry_id_for_service_call(hass: HomeAssistant, call: ServiceCall) -> str: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class PairedSensorManager:
    _api_lock: Incomplete
    _client: Incomplete
    _entry: Incomplete
    _hass: Incomplete
    _paired_uids: Incomplete
    _sensor_pair_dump_coordinator: Incomplete
    coordinators: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, client: Client, api_lock: asyncio.Lock, sensor_pair_dump_coordinator: GuardianDataUpdateCoordinator) -> None: ...
    async def async_initialize(self) -> None: ...
    async def async_pair_sensor(self, uid: str) -> None: ...
    async def async_process_latest_paired_sensor_uids(self) -> None: ...
    async def async_unpair_sensor(self, uid: str) -> None: ...

class GuardianEntity(CoordinatorEntity[GuardianDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_extra_state_attributes: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: GuardianDataUpdateCoordinator, description: EntityDescription) -> None: ...
    def _async_update_from_latest_data(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...

class PairedSensorEntity(GuardianEntity):
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entry: ConfigEntry, coordinator: GuardianDataUpdateCoordinator, description: EntityDescription) -> None: ...

@dataclass
class ValveControllerEntityDescriptionMixin:
    api_category: str
    def __init__(self, api_category) -> None: ...

@dataclass
class ValveControllerEntityDescription(EntityDescription, ValveControllerEntityDescriptionMixin):
    def __init__(self, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class ValveControllerEntity(GuardianEntity):
    _diagnostics_coordinator: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entry: ConfigEntry, coordinators: dict[str, GuardianDataUpdateCoordinator], description: ValveControllerEntityDescription) -> None: ...
