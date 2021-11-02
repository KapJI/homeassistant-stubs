from .const import AUTH as AUTH, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, WEBHOOK_ACTIVATION as WEBHOOK_ACTIVATION, WEBHOOK_DEACTIVATION as WEBHOOK_DEACTIVATION, WEBHOOK_NACAMERA_CONNECTION as WEBHOOK_NACAMERA_CONNECTION, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from typing import Any

_LOGGER: Any
CAMERA_DATA_CLASS_NAME: str
WEATHERSTATION_DATA_CLASS_NAME: str
HOMECOACH_DATA_CLASS_NAME: str
HOMEDATA_DATA_CLASS_NAME: str
HOMESTATUS_DATA_CLASS_NAME: str
PUBLICDATA_DATA_CLASS_NAME: str
DATA_CLASSES: Any
BATCH_SIZE: int
DEFAULT_INTERVALS: Any
SCAN_INTERVAL: int

class NetatmoDataClass:
    name: str
    interval: int
    next_scan: float
    subscriptions: list[CALLBACK_TYPE]

class NetatmoDataHandler:
    hass: Any
    _auth: Any
    listeners: Any
    data_classes: Any
    data: Any
    _queue: Any
    _webhook: bool
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def async_setup(self) -> None: ...
    async def async_update(self, event_time: timedelta) -> None: ...
    def async_force_update(self, data_class_entry: str) -> None: ...
    async def async_cleanup(self) -> None: ...
    async def handle_event(self, event: dict) -> None: ...
    async def async_fetch_data(self, data_class_entry: str) -> None: ...
    async def register_data_class(self, data_class_name: str, data_class_entry: str, update_callback: CALLBACK_TYPE, **kwargs: Any) -> None: ...
    async def unregister_data_class(self, data_class_entry: str, update_callback: Union[CALLBACK_TYPE, None]) -> None: ...
    @property
    def webhook(self) -> bool: ...
