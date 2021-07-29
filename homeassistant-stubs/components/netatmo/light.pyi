import pyatmo
from .const import DATA_HANDLER as DATA_HANDLER, DOMAIN as DOMAIN, EVENT_TYPE_LIGHT_MODE as EVENT_TYPE_LIGHT_MODE, MANUFACTURER as MANUFACTURER, SIGNAL_NAME as SIGNAL_NAME, WEBHOOK_LIGHT_MODE as WEBHOOK_LIGHT_MODE, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from .data_handler import CAMERA_DATA_CLASS_NAME as CAMERA_DATA_CLASS_NAME, NetatmoDataHandler as NetatmoDataHandler
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from homeassistant.components.light import LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoLight(NetatmoBase, LightEntity):
    _id: Any
    _home_id: Any
    _model: Any
    _device_name: Any
    _attr_name: Any
    _is_on: bool
    _attr_unique_id: Any
    def __init__(self, data_handler: NetatmoDataHandler, camera_id: str, camera_type: str, home_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def handle_event(self, event: dict) -> None: ...
    @property
    def _data(self) -> pyatmo.AsyncCameraData: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: dict) -> None: ...
    async def async_turn_off(self, **kwargs: dict) -> None: ...
    def async_update_callback(self) -> None: ...
