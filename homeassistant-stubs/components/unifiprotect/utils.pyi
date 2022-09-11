from .const import DOMAIN as DOMAIN, ModelType as ModelType
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from pyunifiprotect.data import Bootstrap as Bootstrap, Light as Light, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel
from typing import Any

MAC_RE: Incomplete

def get_nested_attr(obj: Any, attr: str) -> Any: ...
def async_unifi_mac(mac: str) -> str: ...
def async_short_mac(mac: str) -> str: ...
async def _async_resolve(hass: HomeAssistant, host: str) -> Union[str, None]: ...
def async_get_devices_by_type(bootstrap: Bootstrap, device_type: ModelType) -> dict[str, ProtectAdoptableDeviceModel]: ...
def async_get_light_motion_current(obj: Light) -> str: ...
def async_dispatch_id(entry: ConfigEntry, dispatch: str) -> str: ...
def convert_mac_list(option: str, raise_exception: bool = ...) -> set[str]: ...
