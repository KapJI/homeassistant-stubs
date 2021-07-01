from .const import LEASES_REGEX as LEASES_REGEX
from .model import Device as Device
from homeassistant.components.device_tracker import DOMAIN as DOMAIN, DeviceScanner as DeviceScanner
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final

_LOGGER: Final[Any]
PLATFORM_SCHEMA: Final[Any]

def get_scanner(hass: HomeAssistant, config: ConfigType) -> Union[DeviceScanner, None]: ...

class ActiontecDeviceScanner(DeviceScanner):
    host: Any
    username: Any
    password: Any
    last_results: Any
    success_init: Any
    def __init__(self, config: ConfigType) -> None: ...
    def scan_devices(self) -> list[str]: ...
    def get_device_name(self, device: str) -> Union[str, None]: ...
    def _update_info(self) -> bool: ...
    def get_actiontec_data(self) -> Union[list[Device], None]: ...
