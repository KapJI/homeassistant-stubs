from .const import DEVICE_SUPPORT as DEVICE_SUPPORT, DOMAIN as DOMAIN, MANUFACTURER_EDS as MANUFACTURER_EDS, MANUFACTURER_HOBBYBOARDS as MANUFACTURER_HOBBYBOARDS, MANUFACTURER_MAXIM as MANUFACTURER_MAXIM
from .model import OWDeviceDescription as OWDeviceDescription
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, ATTR_VIA_DEVICE as ATTR_VIA_DEVICE, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo

DEVICE_COUPLERS: Incomplete
DEVICE_MANUFACTURER: Incomplete
_LOGGER: Incomplete

def _is_known_device(device_family: str, device_type: str) -> bool: ...

class OneWireHub:
    hass: Incomplete
    owproxy: Incomplete
    devices: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def connect(self, host: str, port: int) -> None: ...
    async def initialize(self, config_entry: ConfigEntry) -> None: ...
    async def discover_devices(self) -> None: ...
    def _discover_devices(self, path: str = '/', parent_id: str | None = None) -> list[OWDeviceDescription]: ...
    def _get_device_type(self, device_path: str) -> str: ...

class CannotConnect(HomeAssistantError): ...
class InvalidPath(HomeAssistantError): ...
