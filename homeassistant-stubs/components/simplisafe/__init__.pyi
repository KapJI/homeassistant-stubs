import asyncio
from .const import ATTR_LAST_EVENT_INFO as ATTR_LAST_EVENT_INFO, ATTR_LAST_EVENT_SENSOR_NAME as ATTR_LAST_EVENT_SENSOR_NAME, ATTR_LAST_EVENT_SENSOR_TYPE as ATTR_LAST_EVENT_SENSOR_TYPE, ATTR_LAST_EVENT_TIMESTAMP as ATTR_LAST_EVENT_TIMESTAMP, ATTR_SYSTEM_ID as ATTR_SYSTEM_ID, DISPATCHER_TOPIC_WEBSOCKET_EVENT as DISPATCHER_TOPIC_WEBSOCKET_EVENT, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import SimpliSafeDataUpdateCoordinator as SimpliSafeDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from .typing import SystemType as SystemType
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CODE as ATTR_CODE, CONF_CODE as CONF_CODE, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import UpdateFailed as UpdateFailed
from simplipy import API
from simplipy.system import SystemNotification as SystemNotification
from simplipy.websocket import WebsocketEvent as WebsocketEvent
from typing import Any

type SimpliSafeConfigEntry = ConfigEntry[SimpliSafe]
ATTR_CATEGORY: str
ATTR_LAST_EVENT_CHANGED_BY: str
ATTR_LAST_EVENT_SENSOR_SERIAL: str
ATTR_LAST_EVENT_TYPE: str
ATTR_MESSAGE: str
ATTR_TIMESTAMP: str
WEBSOCKET_RECONNECT_RETRIES: int
WEBSOCKET_RETRY_DELAY: int
WEBSOCKET_LOOP_TASK_NAME: str
EVENT_SIMPLISAFE_EVENT: str
EVENT_SIMPLISAFE_NOTIFICATION: str
PLATFORMS: Incomplete
WEBSOCKET_EVENTS_TO_FIRE_HASS_EVENT: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def _async_register_base_station(hass: HomeAssistant, entry: ConfigEntry, system: SystemType) -> None: ...
@callback
def _async_standardize_config_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: SimpliSafeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SimpliSafeConfigEntry) -> bool: ...

class SimpliSafe:
    _api: Incomplete
    _hass: Incomplete
    _system_notifications: dict[int, set[SystemNotification]]
    _websocket_task: asyncio.Task | None
    entry: Incomplete
    initial_event_to_use: dict[int, dict[str, Any]]
    subscription_data: dict[int, Any]
    systems: dict[int, SystemType]
    coordinator: SimpliSafeDataUpdateCoordinator | None
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, api: API) -> None: ...
    @callback
    def _async_process_new_notifications(self, system: SystemType) -> None: ...
    @callback
    def _async_start_websocket_if_needed(self) -> None: ...
    async def _async_websocket_loop(self) -> None: ...
    async def _async_cancel_websocket_loop(self) -> None: ...
    @callback
    def _async_websocket_on_event(self, event: WebsocketEvent) -> None: ...
    async def async_init(self) -> None: ...
    async def async_update(self) -> None: ...
