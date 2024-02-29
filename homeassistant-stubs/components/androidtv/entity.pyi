from . import ADB_PYTHON_EXCEPTIONS as ADB_PYTHON_EXCEPTIONS, ADB_TCP_EXCEPTIONS as ADB_TCP_EXCEPTIONS, get_androidtv_mac as get_androidtv_mac
from .const import DEVICE_ANDROIDTV as DEVICE_ANDROIDTV, DOMAIN as DOMAIN
from _typeshed import Incomplete
from androidtv.setup_async import AndroidTVAsync as AndroidTVAsync, FireTVAsync as FireTVAsync
from collections.abc import Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from typing import Any, ParamSpec, TypeVar

PREFIX_ANDROIDTV: str
PREFIX_FIRETV: str
_LOGGER: Incomplete
_ADBDeviceT = TypeVar('_ADBDeviceT', bound='AndroidTVEntity')
_R = TypeVar('_R')
_P = ParamSpec('_P')
_FuncType: Incomplete
_ReturnFuncType: Incomplete

def adb_decorator(override_available: bool = False) -> Callable[[_FuncType[_ADBDeviceT, _P, _R]], _ReturnFuncType[_ADBDeviceT, _P, _R]]: ...

class AndroidTVEntity(Entity):
    _attr_has_entity_name: bool
    aftv: Incomplete
    _attr_unique_id: Incomplete
    _entry_data: Incomplete
    _attr_device_info: Incomplete
    exceptions: Incomplete
    def __init__(self, aftv: AndroidTVAsync | FireTVAsync, entry: ConfigEntry, entry_data: dict[str, Any]) -> None: ...
