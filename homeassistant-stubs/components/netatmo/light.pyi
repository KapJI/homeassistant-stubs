from .const import CONF_URL_CONTROL as CONF_URL_CONTROL, CONF_URL_SECURITY as CONF_URL_SECURITY, DOMAIN as DOMAIN, EVENT_TYPE_LIGHT_MODE as EVENT_TYPE_LIGHT_MODE, NETATMO_CREATE_CAMERA_LIGHT as NETATMO_CREATE_CAMERA_LIGHT, NETATMO_CREATE_LIGHT as NETATMO_CREATE_LIGHT, WEBHOOK_LIGHT_MODE as WEBHOOK_LIGHT_MODE, WEBHOOK_PUSH_TYPE as WEBHOOK_PUSH_TYPE
from .data_handler import HOME as HOME, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .netatmo_entity_base import NetatmoBase as NetatmoBase
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NetatmoCameraLight(NetatmoBase, LightEntity):
    _attr_has_entity_name: bool
    _camera: Incomplete
    _id: Incomplete
    _home_id: Incomplete
    _device_name: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _is_on: bool
    _attr_unique_id: Incomplete
    _signal_name: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def handle_event(self, event: dict) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def async_update_callback(self) -> None: ...

class NetatmoLight(NetatmoBase, LightEntity):
    _dimmer: Incomplete
    _id: Incomplete
    _home_id: Incomplete
    _device_name: Incomplete
    _attr_name: Incomplete
    _model: Incomplete
    _config_url: Incomplete
    _attr_brightness: int
    _attr_unique_id: Incomplete
    _attr_supported_color_modes: Incomplete
    _signal_name: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def async_update_callback(self) -> None: ...
