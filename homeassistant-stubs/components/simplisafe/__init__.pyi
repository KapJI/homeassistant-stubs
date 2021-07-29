from .const import ATTR_ALARM_DURATION as ATTR_ALARM_DURATION, ATTR_ALARM_VOLUME as ATTR_ALARM_VOLUME, ATTR_CHIME_VOLUME as ATTR_CHIME_VOLUME, ATTR_ENTRY_DELAY_AWAY as ATTR_ENTRY_DELAY_AWAY, ATTR_ENTRY_DELAY_HOME as ATTR_ENTRY_DELAY_HOME, ATTR_EXIT_DELAY_AWAY as ATTR_EXIT_DELAY_AWAY, ATTR_EXIT_DELAY_HOME as ATTR_EXIT_DELAY_HOME, ATTR_LIGHT as ATTR_LIGHT, ATTR_VOICE_PROMPT_VOLUME as ATTR_VOICE_PROMPT_VOLUME, DATA_CLIENT as DATA_CLIENT, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, LOGGER as LOGGER, VOLUMES as VOLUMES
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CODE as ATTR_CODE, CONF_CODE as CONF_CODE, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service, verify_domain_control as verify_domain_control
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from simplipy.api import API as API
from simplipy.sensor.v2 import SensorV2 as SensorV2
from simplipy.sensor.v3 import SensorV3 as SensorV3
from simplipy.system import SystemNotification as SystemNotification
from simplipy.system.v2 import SystemV2 as SystemV2
from simplipy.system.v3 import SystemV3
from typing import Any

EVENT_SIMPLISAFE_NOTIFICATION: str
DEFAULT_SOCKET_MIN_RETRY: int
PLATFORMS: Any
ATTR_CATEGORY: str
ATTR_MESSAGE: str
ATTR_PIN_LABEL: str
ATTR_PIN_LABEL_OR_VALUE: str
ATTR_PIN_VALUE: str
ATTR_SYSTEM_ID: str
ATTR_TIMESTAMP: str
SERVICE_BASE_SCHEMA: Any
SERVICE_REMOVE_PIN_SCHEMA: Any
SERVICE_SET_PIN_SCHEMA: Any
SERVICE_SET_SYSTEM_PROPERTIES_SCHEMA: Any
CONFIG_SCHEMA: Any

async def async_get_client_id(hass: HomeAssistant) -> str: ...
async def async_register_base_station(hass: HomeAssistant, system: Union[SystemV2, SystemV3], config_entry_id: str) -> None: ...
def _async_standardize_config_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_reload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...

class SimpliSafe:
    _api: Any
    _hass: Any
    _system_notifications: Any
    config_entry: Any
    coordinator: Any
    systems: Any
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, api: API) -> None: ...
    def _async_process_new_notifications(self, system: Union[SystemV2, SystemV3]) -> None: ...
    async def async_init(self) -> None: ...
    async def async_update(self) -> None: ...

class SimpliSafeEntity(CoordinatorEntity):
    _serial: Any
    _attr_extra_state_attributes: Any
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    _online: bool
    _simplisafe: Any
    _system: Any
    def __init__(self, simplisafe: SimpliSafe, system: Union[SystemV2, SystemV3], name: str, *, serial: Union[str, None] = ...) -> None: ...
    @property
    def available(self) -> bool: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def async_update_from_rest_api(self) -> None: ...

class SimpliSafeBaseSensor(SimpliSafeEntity):
    _attr_device_info: Any
    _attr_name: Any
    _sensor: Any
    def __init__(self, simplisafe: SimpliSafe, system: Union[SystemV2, SystemV3], sensor: Union[SensorV2, SensorV3]) -> None: ...
