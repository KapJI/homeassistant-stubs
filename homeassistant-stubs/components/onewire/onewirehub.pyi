from .const import DEVICE_SUPPORT as DEVICE_SUPPORT, DOMAIN as DOMAIN, MANUFACTURER_EDS as MANUFACTURER_EDS, MANUFACTURER_HOBBYBOARDS as MANUFACTURER_HOBBYBOARDS, MANUFACTURER_MAXIM as MANUFACTURER_MAXIM
from .model import OWDeviceDescription as OWDeviceDescription
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_VIA_DEVICE as ATTR_VIA_DEVICE, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.util.signal_type import SignalType as SignalType
from pyownet import protocol

DEVICE_COUPLERS: Incomplete
DEVICE_MANUFACTURER: Incomplete
_DEVICE_SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete
type OneWireConfigEntry = ConfigEntry[OneWireHub]
SIGNAL_NEW_DEVICE_CONNECTED: Incomplete

def _is_known_device(device_family: str, device_type: str | None) -> bool: ...

class OneWireHub:
    owproxy: protocol._Proxy
    devices: list[OWDeviceDescription]
    _version: str | None
    _hass: Incomplete
    _config_entry: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: OneWireConfigEntry) -> None: ...
    def _initialize(self) -> None: ...
    async def initialize(self) -> None: ...
    @callback
    def _populate_device_registry(self, devices: list[OWDeviceDescription]) -> None: ...
    def schedule_scan_for_new_devices(self) -> None: ...
    async def _scan_for_new_devices(self, _: datetime) -> None: ...

def _discover_devices(owproxy: protocol._Proxy, path: str = '/', parent_id: str | None = None) -> list[OWDeviceDescription]: ...
def _get_device_type(owproxy: protocol._Proxy, device_path: str) -> str | None: ...
