from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SENSOR_BATTERY as SENSOR_BATTERY, SENSOR_DOOR as SENSOR_DOOR, SENSOR_GARAGE_DOOR as SENSOR_GARAGE_DOOR, SENSOR_LEAK as SENSOR_LEAK, SENSOR_MISSING as SENSOR_MISSING, SENSOR_SAFE as SENSOR_SAFE, SENSOR_SLIDING as SENSOR_SLIDING, SENSOR_SMOKE_CO as SENSOR_SMOKE_CO, SENSOR_TEMPERATURE as SENSOR_TEMPERATURE, SENSOR_WINDOW_HINGED as SENSOR_WINDOW_HINGED
from _typeshed import Incomplete
from aionotion.bridge.models import Bridge as Bridge, BridgeAllResponse
from aionotion.sensor.models import Listener as Listener, ListenerAllResponse, ListenerKind, Sensor as Sensor, SensorAllResponse
from aionotion.user.models import UserPreferences as UserPreferences, UserPreferencesResponse
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

PLATFORMS: Incomplete
ATTR_SYSTEM_MODE: str
ATTR_SYSTEM_NAME: str
DATA_BRIDGES: str
DATA_LISTENERS: str
DATA_SENSORS: str
DATA_USER_PREFERENCES: str
DEFAULT_SCAN_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete
TASK_TYPE_TO_LISTENER_MAP: dict[str, ListenerKind]

def is_uuid(value: str) -> bool: ...

@dataclass
class NotionData:
    hass: HomeAssistant
    entry: ConfigEntry
    bridges: dict[int, Bridge] = ...
    listeners: dict[str, Listener] = ...
    sensors: dict[str, Sensor] = ...
    user_preferences: UserPreferences | None = ...
    def update_data_from_response(self, response: BridgeAllResponse | ListenerAllResponse | SensorAllResponse | UserPreferencesResponse) -> None: ...
    def asdict(self) -> dict[str, Any]: ...
    def __init__(self, hass, entry, bridges, listeners, sensors, user_preferences) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _async_register_new_bridge(hass: HomeAssistant, entry: ConfigEntry, bridge: Bridge) -> None: ...

class NotionEntity(CoordinatorEntity[DataUpdateCoordinator[NotionData]]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _bridge_id: Incomplete
    _listener_id: Incomplete
    _sensor_id: Incomplete
    _system_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[NotionData], listener_id: str, sensor_id: str, bridge_id: int, system_id: str, description: EntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def listener(self) -> Listener: ...
    def _async_update_bridge_id(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
