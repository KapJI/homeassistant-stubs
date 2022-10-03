import pyatmo
from .const import AUTH as AUTH, DATA_PERSONS as DATA_PERSONS, DATA_SCHEDULES as DATA_SCHEDULES, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, NETATMO_CREATE_BATTERY as NETATMO_CREATE_BATTERY, NETATMO_CREATE_CAMERA as NETATMO_CREATE_CAMERA, NETATMO_CREATE_CAMERA_LIGHT as NETATMO_CREATE_CAMERA_LIGHT, NETATMO_CREATE_CLIMATE as NETATMO_CREATE_CLIMATE, NETATMO_CREATE_COVER as NETATMO_CREATE_COVER, NETATMO_CREATE_LIGHT as NETATMO_CREATE_LIGHT, NETATMO_CREATE_ROOM_SENSOR as NETATMO_CREATE_ROOM_SENSOR, NETATMO_CREATE_SELECT as NETATMO_CREATE_SELECT, NETATMO_CREATE_SENSOR as NETATMO_CREATE_SENSOR, NETATMO_CREATE_SWITCH as NETATMO_CREATE_SWITCH, NETATMO_CREATE_WEATHER_SENSOR as NETATMO_CREATE_WEATHER_SENSOR, PLATFORMS as PLATFORMS, WEBHOOK_ACTIVATION as WEBHOOK_ACTIVATION, WEBHOOK_DEACTIVATION as WEBHOOK_DEACTIVATION, WEBHOOK_NACAMERA_CONNECTION as WEBHOOK_NACAMERA_CONNECTION, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from typing import Any

_LOGGER: Incomplete
SIGNAL_NAME: str
ACCOUNT: str
HOME: str
WEATHER: str
AIR_CARE: str
PUBLIC: str
EVENT: str
PUBLISHERS: Incomplete
BATCH_SIZE: int
DEFAULT_INTERVALS: Incomplete
SCAN_INTERVAL: int

class NetatmoDevice:
    data_handler: NetatmoDataHandler
    device: pyatmo.modules.Module
    parent_id: str
    signal_name: str
    def __init__(self, data_handler, device, parent_id, signal_name) -> None: ...

class NetatmoHome:
    data_handler: NetatmoDataHandler
    home: pyatmo.Home
    parent_id: str
    signal_name: str
    def __init__(self, data_handler, home, parent_id, signal_name) -> None: ...

class NetatmoRoom:
    data_handler: NetatmoDataHandler
    room: pyatmo.Room
    parent_id: str
    signal_name: str
    def __init__(self, data_handler, room, parent_id, signal_name) -> None: ...

class NetatmoPublisher:
    name: str
    interval: int
    next_scan: float
    subscriptions: set[Union[CALLBACK_TYPE, None]]
    method: str
    kwargs: dict
    def __init__(self, name, interval, next_scan, subscriptions, method, kwargs) -> None: ...

class NetatmoDataHandler:
    account: pyatmo.AsyncAccount
    hass: Incomplete
    config_entry: Incomplete
    _auth: Incomplete
    publisher: Incomplete
    _queue: Incomplete
    _webhook: bool
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_update(self, event_time: datetime) -> None: ...
    def async_force_update(self, signal_name: str) -> None: ...
    async def handle_event(self, event: dict) -> None: ...
    async def async_fetch_data(self, signal_name: str) -> None: ...
    async def subscribe(self, publisher: str, signal_name: str, update_callback: Union[CALLBACK_TYPE, None], **kwargs: Any) -> None: ...
    async def unsubscribe(self, signal_name: str, update_callback: Union[CALLBACK_TYPE, None]) -> None: ...
    @property
    def webhook(self) -> bool: ...
    async def async_dispatch(self) -> None: ...
    def setup_air_care(self) -> None: ...
    def setup_modules(self, home: pyatmo.Home, signal_home: str) -> None: ...
    def setup_rooms(self, home: pyatmo.Home, signal_home: str) -> None: ...
    def setup_climate_schedule_select(self, home: pyatmo.Home, signal_home: str) -> None: ...
