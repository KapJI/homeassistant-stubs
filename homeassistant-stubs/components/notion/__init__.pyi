from .const import CONF_REFRESH_TOKEN as CONF_REFRESH_TOKEN, CONF_USER_UUID as CONF_USER_UUID, DOMAIN as DOMAIN, LOGGER as LOGGER, SENSOR_BATTERY as SENSOR_BATTERY, SENSOR_DOOR as SENSOR_DOOR, SENSOR_GARAGE_DOOR as SENSOR_GARAGE_DOOR, SENSOR_LEAK as SENSOR_LEAK, SENSOR_MISSING as SENSOR_MISSING, SENSOR_SAFE as SENSOR_SAFE, SENSOR_SLIDING as SENSOR_SLIDING, SENSOR_SMOKE_CO as SENSOR_SMOKE_CO, SENSOR_TEMPERATURE as SENSOR_TEMPERATURE, SENSOR_WINDOW_HINGED as SENSOR_WINDOW_HINGED
from .coordinator import NotionDataUpdateCoordinator as NotionDataUpdateCoordinator
from .util import async_get_client_with_credentials as async_get_client_with_credentials, async_get_client_with_refresh_token as async_get_client_with_refresh_token
from _typeshed import Incomplete
from aionotion.bridge.models import Bridge as Bridge
from aionotion.listener.models import Listener as Listener, ListenerKind
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PLATFORMS: Incomplete
ATTR_SYSTEM_MODE: str
ATTR_SYSTEM_NAME: str
DEFAULT_SCAN_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete
TASK_TYPE_TO_LISTENER_MAP: dict[str, ListenerKind]

def is_uuid(value: str) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class NotionEntity(CoordinatorEntity[NotionDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _bridge_id: Incomplete
    _listener_id: Incomplete
    _sensor_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: NotionDataUpdateCoordinator, listener_id: str, sensor_id: str, bridge_id: int, description: EntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def listener(self) -> Listener: ...
    def _async_get_bridge(self, bridge_id: int) -> Bridge | None: ...
    def _async_update_bridge_id(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
