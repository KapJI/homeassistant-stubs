from _typeshed import Incomplete
from homeassistant.components.device_tracker import DeviceScanner as DeviceScanner
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
_DEVICES_REGEX: Incomplete
PLATFORM_SCHEMA: Incomplete

def get_scanner(hass: HomeAssistant, config: ConfigType) -> ArubaDeviceScanner | None: ...

class ArubaDeviceScanner(DeviceScanner):
    host: Incomplete
    username: Incomplete
    password: Incomplete
    last_results: Incomplete
    success_init: Incomplete
    def __init__(self, config: dict[str, Any]) -> None: ...
    def scan_devices(self) -> list[str]: ...
    def get_device_name(self, device: str) -> str | None: ...
    def _update_info(self) -> bool: ...
    def get_aruba_data(self) -> dict[str, dict[str, str]] | None: ...
