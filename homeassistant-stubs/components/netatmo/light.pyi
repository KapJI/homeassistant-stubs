import pyatmo
from .const import DATA_HANDLER as DATA_HANDLER, DOMAIN as DOMAIN, EVENT_TYPE_LIGHT_MODE as EVENT_TYPE_LIGHT_MODE, SIGNAL_NAME as SIGNAL_NAME, TYPE_SECURITY as TYPE_SECURITY, WEBHOOK_LIGHT_MODE as WEBHOOK_LIGHT_MODE, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from .data_handler import CAMERA_DATA_CLASS_NAME as CAMERA_DATA_CLASS_NAME, NetatmoDataHandler as NetatmoDataHandler
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoLight(NetatmoBase, LightEntity):
    _attr_color_mode: Incomplete
    _attr_has_entity_name: bool
    _attr_supported_color_modes: Incomplete
    _id: Incomplete
    _home_id: Incomplete
    _model: Incomplete
    _netatmo_type: Incomplete
    _device_name: Incomplete
    _is_on: bool
    _attr_unique_id: Incomplete
    def __init__(self, data_handler: NetatmoDataHandler, camera_id: str, camera_type: str, home_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def handle_event(self, event: dict) -> None: ...
    @property
    def _data(self) -> pyatmo.AsyncCameraData: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def async_update_callback(self) -> None: ...
