from .const import ATTR_DURATION as ATTR_DURATION, ATTR_MESSAGE as ATTR_MESSAGE, DOMAIN as DOMAIN, TYPE_EMPTY_VALUE as TYPE_EMPTY_VALUE
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity, async_all_device_entities as async_all_device_entities
from .models import ProtectSetableKeysMixin as ProtectSetableKeysMixin, T as T
from collections.abc import Callable as Callable
from enum import Enum
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.util.dt import utcnow as utcnow
from pyunifiprotect.api import ProtectApiClient as ProtectApiClient
from pyunifiprotect.data import Camera, Doorlock, Light, Sensor, Viewer
from typing import Any, Final

_LOGGER: Any
_KEY_LIGHT_MOTION: str
INFRARED_MODES: Any
CHIME_TYPES: Any
MOUNT_TYPES: Any
LIGHT_MODE_MOTION: str
LIGHT_MODE_MOTION_DARK: str
LIGHT_MODE_DARK: str
LIGHT_MODE_OFF: str
LIGHT_MODES: Any
LIGHT_MODE_TO_SETTINGS: Any
MOTION_MODE_TO_LIGHT_MODE: Any
DEVICE_RECORDING_MODES: Any
DEVICE_CLASS_LCD_MESSAGE: Final[str]
SERVICE_SET_DOORBELL_MESSAGE: str
SET_DOORBELL_LCD_MESSAGE_SCHEMA: Any

class ProtectSelectEntityDescription(ProtectSetableKeysMixin, SelectEntityDescription):
    ufp_options: Union[list[dict[str, Any]], None]
    ufp_options_fn: Union[Callable[[ProtectApiClient], list[dict[str, Any]]], None]
    ufp_enum_type: Union[type[Enum], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, ufp_required_field, ufp_value, ufp_value_fn, ufp_enabled, ufp_set_method, ufp_set_method_fn, ufp_options, ufp_options_fn, ufp_enum_type) -> None: ...

def _get_viewer_options(api: ProtectApiClient) -> list[dict[str, Any]]: ...
def _get_doorbell_options(api: ProtectApiClient) -> list[dict[str, Any]]: ...
def _get_paired_camera_options(api: ProtectApiClient) -> list[dict[str, Any]]: ...
def _get_viewer_current(obj: Viewer) -> str: ...
def _get_light_motion_current(obj: Light) -> str: ...
def _get_doorbell_current(obj: Camera) -> Union[str, None]: ...
async def _set_light_mode(obj: Light, mode: str) -> None: ...
async def _set_paired_camera(obj: Union[Light, Sensor, Doorlock], camera_id: str) -> None: ...
async def _set_doorbell_message(obj: Camera, message: str) -> None: ...
async def _set_liveview(obj: Viewer, liveview_id: str) -> None: ...

CAMERA_SELECTS: tuple[ProtectSelectEntityDescription, ...]
LIGHT_SELECTS: tuple[ProtectSelectEntityDescription, ...]
SENSE_SELECTS: tuple[ProtectSelectEntityDescription, ...]
DOORLOCK_SELECTS: tuple[ProtectSelectEntityDescription, ...]
VIEWER_SELECTS: tuple[ProtectSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: entity_platform.AddEntitiesCallback) -> None: ...

class ProtectSelects(ProtectDeviceEntity, SelectEntity):
    device: Union[Camera, Light, Viewer]
    entity_description: ProtectSelectEntityDescription
    _attr_name: Any
    def __init__(self, data: ProtectData, device: Union[Camera, Light, Viewer], description: ProtectSelectEntityDescription) -> None: ...
    def _async_update_device_from_protect(self) -> None: ...
    _attr_options: Any
    _hass_to_unifi_options: Any
    _unifi_to_hass_options: Any
    def _async_set_options(self) -> None: ...
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
    async def async_set_doorbell_message(self, message: str, duration: str) -> None: ...
