from .const import CONF_SERIAL_PORT as CONF_SERIAL_PORT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import usb as usb
from homeassistant.components.usb import human_readable_device_name as human_readable_device_name
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.helpers.service_info.usb import UsbServiceInfo as UsbServiceInfo
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

class TeleinfoConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    _discovered_device: str | None
    def __init__(self) -> None: ...
    async def _validate_serial_port(self, serial_port: str) -> tuple[dict[str, str], dict[str, str] | None]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_usb(self, discovery_info: UsbServiceInfo) -> ConfigFlowResult: ...
    async def async_step_usb_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
