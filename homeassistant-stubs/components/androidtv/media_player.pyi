from . import ADB_PYTHON_EXCEPTIONS as ADB_PYTHON_EXCEPTIONS, ADB_TCP_EXCEPTIONS as ADB_TCP_EXCEPTIONS, get_androidtv_mac as get_androidtv_mac
from .const import ANDROID_DEV as ANDROID_DEV, ANDROID_DEV_OPT as ANDROID_DEV_OPT, CONF_APPS as CONF_APPS, CONF_EXCLUDE_UNNAMED_APPS as CONF_EXCLUDE_UNNAMED_APPS, CONF_GET_SOURCES as CONF_GET_SOURCES, CONF_SCREENCAP as CONF_SCREENCAP, CONF_TURN_OFF_COMMAND as CONF_TURN_OFF_COMMAND, CONF_TURN_ON_COMMAND as CONF_TURN_ON_COMMAND, DEFAULT_EXCLUDE_UNNAMED_APPS as DEFAULT_EXCLUDE_UNNAMED_APPS, DEFAULT_GET_SOURCES as DEFAULT_GET_SOURCES, DEFAULT_SCREENCAP as DEFAULT_SCREENCAP, DEVICE_ANDROIDTV as DEVICE_ANDROIDTV, DOMAIN as DOMAIN, SIGNAL_CONFIG_ENTITY as SIGNAL_CONFIG_ENTITY
from _typeshed import Incomplete
from androidtv.setup_async import AndroidTVAsync as AndroidTVAsync, FireTVAsync as FireTVAsync
from collections.abc import Callable
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntity as MediaPlayerEntity, MediaPlayerEntityFeature as MediaPlayerEntityFeature, MediaPlayerState as MediaPlayerState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_COMMAND as ATTR_COMMAND, ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import Throttle as Throttle
from typing import Any, ParamSpec, TypeVar

_ADBDeviceT = TypeVar('_ADBDeviceT', bound='ADBDevice')
_R = TypeVar('_R')
_P = ParamSpec('_P')
_LOGGER: Incomplete
ATTR_ADB_RESPONSE: str
ATTR_DEVICE_PATH: str
ATTR_HDMI_INPUT: str
ATTR_LOCAL_PATH: str
MIN_TIME_BETWEEN_SCREENCAPS: Incomplete
SERVICE_ADB_COMMAND: str
SERVICE_DOWNLOAD: str
SERVICE_LEARN_SENDEVENT: str
SERVICE_UPLOAD: str
PREFIX_ANDROIDTV: str
PREFIX_FIRETV: str
ANDROIDTV_STATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_FuncType: Incomplete
_ReturnFuncType: Incomplete

def adb_decorator(override_available: bool = False) -> Callable[[_FuncType[_ADBDeviceT, _P, _R]], _ReturnFuncType[_ADBDeviceT, _P, _R]]: ...

class ADBDevice(MediaPlayerEntity):
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    aftv: Incomplete
    _attr_unique_id: Incomplete
    _entry_id: Incomplete
    _entry_data: Incomplete
    _media_image: Incomplete
    _attr_media_image_hash: Incomplete
    _attr_device_info: Incomplete
    _app_id_to_name: Incomplete
    _app_name_to_id: Incomplete
    _get_sources: Incomplete
    _exclude_unnamed_apps: Incomplete
    _screencap: Incomplete
    turn_on_command: Incomplete
    turn_off_command: Incomplete
    exceptions: Incomplete
    _attr_extra_state_attributes: Incomplete
    _failed_connect_count: int
    def __init__(self, aftv: AndroidTVAsync | FireTVAsync, name: str, dev_type: str, unique_id: str, entry_id: str, entry_data: dict[str, Any]) -> None: ...
    def _process_config(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _adb_screencap(self) -> bytes | None: ...
    async def _async_get_screencap(self, prev_app_id: str | None = None) -> None: ...
    async def _adb_get_screencap(self, **kwargs: Any) -> None: ...
    async def async_get_media_image(self) -> tuple[bytes | None, str | None]: ...
    async def async_media_play(self) -> None: ...
    async def async_media_pause(self) -> None: ...
    async def async_media_play_pause(self) -> None: ...
    async def async_turn_on(self) -> None: ...
    async def async_turn_off(self) -> None: ...
    async def async_media_previous_track(self) -> None: ...
    async def async_media_next_track(self) -> None: ...
    async def async_select_source(self, source: str) -> None: ...
    async def adb_command(self, command: str) -> None: ...
    async def learn_sendevent(self) -> None: ...
    async def service_download(self, device_path: str, local_path: str) -> None: ...
    async def service_upload(self, device_path: str, local_path: str) -> None: ...

class AndroidTVDevice(ADBDevice):
    _attr_supported_features: Incomplete
    aftv: AndroidTVAsync
    _failed_connect_count: int
    _attr_available: bool
    _attr_state: Incomplete
    _attr_source: Incomplete
    _attr_source_list: Incomplete
    async def async_update(self) -> None: ...
    async def async_media_stop(self) -> None: ...
    async def async_mute_volume(self, mute: bool) -> None: ...
    async def async_set_volume_level(self, volume: float) -> None: ...
    _attr_volume_level: Incomplete
    async def async_volume_down(self) -> None: ...
    async def async_volume_up(self) -> None: ...

class FireTVDevice(ADBDevice):
    _attr_supported_features: Incomplete
    aftv: FireTVAsync
    _failed_connect_count: int
    _attr_available: bool
    _attr_state: Incomplete
    _attr_source: Incomplete
    _attr_source_list: Incomplete
    async def async_update(self) -> None: ...
    async def async_media_stop(self) -> None: ...
