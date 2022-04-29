import pyatmo
from .const import AUTH as AUTH, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, WEBHOOK_ACTIVATION as WEBHOOK_ACTIVATION, WEBHOOK_DEACTIVATION as WEBHOOK_DEACTIVATION, WEBHOOK_NACAMERA_CONNECTION as WEBHOOK_NACAMERA_CONNECTION, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from typing import Any

_LOGGER: Incomplete
CAMERA_DATA_CLASS_NAME: str
WEATHERSTATION_DATA_CLASS_NAME: str
HOMECOACH_DATA_CLASS_NAME: str
CLIMATE_TOPOLOGY_CLASS_NAME: str
CLIMATE_STATE_CLASS_NAME: str
PUBLICDATA_DATA_CLASS_NAME: str
DATA_CLASSES: Incomplete
BATCH_SIZE: int
DEFAULT_INTERVALS: Incomplete
SCAN_INTERVAL: int

class NetatmoDevice:
    data_handler: NetatmoDataHandler
    device: pyatmo.climate.NetatmoModule
    parent_id: str
    state_class_name: str
    def __init__(self, data_handler, device, parent_id, state_class_name) -> None: ...

class NetatmoDataClass:
    name: str
    interval: int
    next_scan: float
    subscriptions: list[Union[CALLBACK_TYPE, None]]
    def __init__(self, name, interval, next_scan, subscriptions) -> None: ...

class NetatmoDataHandler:
    hass: Incomplete
    config_entry: Incomplete
    _auth: Incomplete
    data_classes: Incomplete
    data: Incomplete
    _queue: Incomplete
    _webhook: bool
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_update(self, event_time: datetime) -> None: ...
    def async_force_update(self, data_class_entry: str) -> None: ...
    async def handle_event(self, event: dict) -> None: ...
    async def async_fetch_data(self, data_class_entry: str) -> None: ...
    async def register_data_class(self, data_class_name: str, data_class_entry: str, update_callback: Union[CALLBACK_TYPE, None], **kwargs: Any) -> None: ...
    async def unregister_data_class(self, data_class_entry: str, update_callback: Union[CALLBACK_TYPE, None]) -> None: ...
    @property
    def webhook(self) -> bool: ...
