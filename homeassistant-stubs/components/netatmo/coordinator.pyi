import pyatmo
from .const import CAMERA_CONNECTION_WEBHOOKS as CAMERA_CONNECTION_WEBHOOKS, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, NETATMO_CREATE_BUTTON as NETATMO_CREATE_BUTTON, NETATMO_CREATE_CAMERA as NETATMO_CREATE_CAMERA, NETATMO_CREATE_CAMERA_LIGHT as NETATMO_CREATE_CAMERA_LIGHT, NETATMO_CREATE_CLIMATE as NETATMO_CREATE_CLIMATE, NETATMO_CREATE_CLIMATE_BATTERY_SENSOR as NETATMO_CREATE_CLIMATE_BATTERY_SENSOR, NETATMO_CREATE_CONNECTIVITY_BINARY_SENSOR as NETATMO_CREATE_CONNECTIVITY_BINARY_SENSOR, NETATMO_CREATE_COVER as NETATMO_CREATE_COVER, NETATMO_CREATE_FAN as NETATMO_CREATE_FAN, NETATMO_CREATE_LEGACY_SENSOR as NETATMO_CREATE_LEGACY_SENSOR, NETATMO_CREATE_LIGHT as NETATMO_CREATE_LIGHT, NETATMO_CREATE_OPENING_BINARY_SENSOR as NETATMO_CREATE_OPENING_BINARY_SENSOR, NETATMO_CREATE_ROOM_SENSOR as NETATMO_CREATE_ROOM_SENSOR, NETATMO_CREATE_SELECT as NETATMO_CREATE_SELECT, NETATMO_CREATE_SENSOR as NETATMO_CREATE_SENSOR, NETATMO_CREATE_SWITCH as NETATMO_CREATE_SWITCH, NETATMO_CREATE_WEATHER_BINARY_SENSOR as NETATMO_CREATE_WEATHER_BINARY_SENSOR, NETATMO_CREATE_WEATHER_SENSOR as NETATMO_CREATE_WEATHER_SENSOR, PLATFORMS as PLATFORMS, WEBHOOK_ACTIVATION as WEBHOOK_ACTIVATION, WEBHOOK_DEACTIVATION as WEBHOOK_DEACTIVATION, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from .device import async_disabled_netatmo_ids as async_disabled_netatmo_ids, async_register_parent_devices as async_register_parent_devices, async_sync_home_disabled_state as async_sync_home_disabled_state, netatmo_module_parents as netatmo_module_parents
from _typeshed import Incomplete
from collections import deque
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components import cloud as cloud
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import EventDeviceRegistryUpdatedData as EventDeviceRegistryUpdatedData
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_device_registry_updated_event as async_track_device_registry_updated_event, async_track_time_interval as async_track_time_interval
from pyatmo.schedule import Schedule as Schedule
from typing import Any

_LOGGER: Incomplete
SIGNAL_NAME: str
ACCOUNT: str
HOME: str
WEATHER: str
AIR_CARE: str
PUBLIC: Incomplete
EVENT: str
PUBLISHERS: Incomplete
BATCH_SIZE: int
DEV_FACTOR: int
DEV_LIMIT: int
CLOUD_FACTOR: int
CLOUD_LIMIT: int
DEFAULT_INTERVALS: Incomplete
SCAN_INTERVAL: int
UNAVAILABLE_AFTER_ERRORS: int
MAX_ERROR_BACKOFF: int
type NetatmoConfigEntry = ConfigEntry[NetatmoDataHandler]

def async_get_loaded_entry(hass: HomeAssistant) -> NetatmoConfigEntry | None: ...

@dataclass
class NetatmoDevice:
    data_handler: NetatmoDataHandler
    device: pyatmo.modules.Module
    parent_id: str
    signal_name: str

@dataclass
class NetatmoHome:
    data_handler: NetatmoDataHandler
    home: pyatmo.Home
    parent_id: str
    signal_name: str

@dataclass
class NetatmoRoom:
    data_handler: NetatmoDataHandler
    room: pyatmo.Room
    parent_id: str
    signal_name: str

@dataclass
class NetatmoPublisher:
    name: str
    interval: int
    next_scan: float
    subscriptions: set[CALLBACK_TYPE | None]
    method: str
    kwargs: dict
    available: bool = ...
    error_count: int = ...
    unavailable_logged: bool = ...

class NetatmoDataHandler:
    account: pyatmo.AsyncAccount
    _interval_factor: int
    hass: Incomplete
    config_entry: Incomplete
    auth: Incomplete
    publisher: dict[str, NetatmoPublisher]
    _queue: deque
    _webhook: bool
    _rate_limit: Incomplete
    poll_start: Incomplete
    poll_count: int
    persons: dict[str, dict[str, str | None]]
    schedules: dict[str, dict[str, Schedule]]
    device_ids: dict[str, str]
    cameras: dict[str, str]
    events: dict[str, dict]
    parent_device_ids: dict[str, str]
    module_parents: dict[str, str]
    home_device_ids: list[str]
    def __init__(self, hass: HomeAssistant, config_entry: NetatmoConfigEntry, auth: pyatmo.AbstractAsyncAuth) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_update(self, event_time: datetime) -> None: ...
    @callback
    def async_force_update(self, signal_name: str) -> None: ...
    async def handle_event(self, event: dict) -> None: ...
    async def async_fetch_data(self, signal_name: str) -> bool: ...
    def _notify_subscribers(self, signal_name: str) -> None: ...
    def is_signal_available(self, signal_name: str) -> bool: ...
    async def subscribe(self, publisher: str, signal_name: str, update_callback: CALLBACK_TYPE | None, **kwargs: Any) -> None: ...
    async def unsubscribe(self, signal_name: str, update_callback: CALLBACK_TYPE | None) -> None: ...
    @property
    def webhook(self) -> bool: ...
    async def async_dispatch(self) -> None: ...
    @callback
    def _handle_home_device_update(self, event: Event[EventDeviceRegistryUpdatedData]) -> None: ...
    def setup_air_care(self) -> None: ...
    def setup_modules(self, home: pyatmo.Home, signal_home: str) -> None: ...
    def setup_rooms(self, home: pyatmo.Home, signal_home: str) -> None: ...
    def setup_climate_schedule_select(self, home: pyatmo.Home, signal_home: str) -> None: ...
