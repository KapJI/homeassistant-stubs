from .const import ATTR_ALARM_DURATION as ATTR_ALARM_DURATION, ATTR_ALARM_VOLUME as ATTR_ALARM_VOLUME, ATTR_CHIME_VOLUME as ATTR_CHIME_VOLUME, ATTR_ENTRY_DELAY_AWAY as ATTR_ENTRY_DELAY_AWAY, ATTR_ENTRY_DELAY_HOME as ATTR_ENTRY_DELAY_HOME, ATTR_EXIT_DELAY_AWAY as ATTR_EXIT_DELAY_AWAY, ATTR_EXIT_DELAY_HOME as ATTR_EXIT_DELAY_HOME, ATTR_LIGHT as ATTR_LIGHT, ATTR_VOICE_PROMPT_VOLUME as ATTR_VOICE_PROMPT_VOLUME, CONF_USER_ID as CONF_USER_ID, DOMAIN as DOMAIN, LOGGER as LOGGER
from .typing import SystemType as SystemType
from collections.abc import Callable as Callable, Iterable
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_CODE as ATTR_CODE, ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_CODE as CONF_CODE, CONF_TOKEN as CONF_TOKEN, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service, verify_domain_control as verify_domain_control
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from simplipy import API
from simplipy.device import Device as Device
from simplipy.system import SystemNotification as SystemNotification
from simplipy.websocket import WebsocketEvent as WebsocketEvent
from typing import Any

ATTR_CATEGORY: str
ATTR_LAST_EVENT_CHANGED_BY: str
ATTR_LAST_EVENT_INFO: str
ATTR_LAST_EVENT_SENSOR_NAME: str
ATTR_LAST_EVENT_SENSOR_SERIAL: str
ATTR_LAST_EVENT_SENSOR_TYPE: str
ATTR_LAST_EVENT_TIMESTAMP: str
ATTR_LAST_EVENT_TYPE: str
ATTR_MESSAGE: str
ATTR_PIN_LABEL: str
ATTR_PIN_LABEL_OR_VALUE: str
ATTR_PIN_VALUE: str
ATTR_SYSTEM_ID: str
ATTR_TIMESTAMP: str
DEFAULT_CONFIG_URL: str
DEFAULT_ENTITY_MODEL: str
DEFAULT_ENTITY_NAME: str
DEFAULT_ERROR_THRESHOLD: int
DEFAULT_SCAN_INTERVAL: Any
DEFAULT_SOCKET_MIN_RETRY: int
DISPATCHER_TOPIC_WEBSOCKET_EVENT: str
EVENT_SIMPLISAFE_EVENT: str
EVENT_SIMPLISAFE_NOTIFICATION: str
PLATFORMS: Any
VOLUME_MAP: Any
SERVICE_NAME_CLEAR_NOTIFICATIONS: str
SERVICE_NAME_REMOVE_PIN: str
SERVICE_NAME_SET_PIN: str
SERVICE_NAME_SET_SYSTEM_PROPERTIES: str
SERVICES: Any
SERVICE_CLEAR_NOTIFICATIONS_SCHEMA: Any
SERVICE_REMOVE_PIN_SCHEMA: Any
SERVICE_SET_PIN_SCHEMA: Any
SERVICE_SET_SYSTEM_PROPERTIES_SCHEMA: Any
WEBSOCKET_EVENTS_REQUIRING_SERIAL: Any
WEBSOCKET_EVENTS_TO_FIRE_HASS_EVENT: Any
CONFIG_SCHEMA: Any

def _async_get_system_for_service_call(hass: HomeAssistant, call: ServiceCall) -> SystemType: ...
def _async_register_base_station(hass: HomeAssistant, entry: ConfigEntry, system: SystemType) -> None: ...
def _async_standardize_config_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SimpliSafe:
    _api: Any
    _hass: Any
    _system_notifications: Any
    _websocket_reconnect_task: Any
    entry: Any
    initial_event_to_use: Any
    subscription_data: Any
    systems: Any
    coordinator: Any
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, api: API) -> None: ...
    def _async_process_new_notifications(self, system: SystemType) -> None: ...
    async def _async_start_websocket_loop(self) -> None: ...
    async def _async_cancel_websocket_loop(self) -> None: ...
    def _async_websocket_on_event(self, event: WebsocketEvent) -> None: ...
    async def async_init(self) -> None: ...
    async def async_update(self) -> None: ...

class SimpliSafeEntity(CoordinatorEntity):
    _error_count: int
    _attr_extra_state_attributes: Any
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    _device: Any
    _online: bool
    _simplisafe: Any
    _system: Any
    _websocket_events_to_listen_for: Any
    def __init__(self, simplisafe: SimpliSafe, system: SystemType, *, device: Union[Device, None] = ..., additional_websocket_events: Union[Iterable[str], None] = ...) -> None: ...
    @property
    def available(self) -> bool: ...
    def _handle_coordinator_update(self) -> None: ...
    def _handle_websocket_update(self, event: WebsocketEvent) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def async_increment_error_count(self) -> None: ...
    def async_reset_error_count(self) -> None: ...
    def async_update_from_rest_api(self) -> None: ...
    def async_update_from_websocket_event(self, event: WebsocketEvent) -> None: ...
