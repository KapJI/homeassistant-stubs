from _typeshed import Incomplete
from arris_tg2492lg import ConnectBox, Device as Device
from homeassistant.components.device_tracker import DOMAIN as DOMAIN, DeviceScanner as DeviceScanner
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

DEFAULT_HOST: str
PLATFORM_SCHEMA: Incomplete

def get_scanner(hass: HomeAssistant, config: ConfigType) -> ArrisDeviceScanner: ...

class ArrisDeviceScanner(DeviceScanner):
    connect_box: Incomplete
    last_results: Incomplete
    def __init__(self, connect_box: ConnectBox) -> None: ...
    def scan_devices(self) -> list[str]: ...
    def get_device_name(self, device: str) -> str | None: ...
    def _update_info(self) -> None: ...
