from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverEntity as CoverEntity, DEVICE_CLASS_BLIND as DEVICE_CLASS_BLIND, DEVICE_CLASS_GARAGE as DEVICE_CLASS_GARAGE, DEVICE_CLASS_SHUTTER as DEVICE_CLASS_SHUTTER, DEVICE_CLASS_WINDOW as DEVICE_CLASS_WINDOW, SUPPORT_CLOSE as SUPPORT_CLOSE, SUPPORT_OPEN as SUPPORT_OPEN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.client import Client as ZwaveClient

LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def percent_to_zwave_position(value: int) -> int: ...

class ZWaveCover(ZWaveBaseEntity, CoverEntity):
    _attr_device_class: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def is_closed(self) -> Union[bool, None]: ...
    @property
    def current_cover_position(self) -> Union[int, None]: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...

class ZwaveMotorizedBarrier(ZWaveBaseEntity, CoverEntity):
    _attr_supported_features: Any
    _attr_device_class: Any
    _target_state: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def is_opening(self) -> Union[bool, None]: ...
    @property
    def is_closing(self) -> Union[bool, None]: ...
    @property
    def is_closed(self) -> Union[bool, None]: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
