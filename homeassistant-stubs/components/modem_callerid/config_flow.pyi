from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, EXCEPTIONS as EXCEPTIONS
from _typeshed import Incomplete
from homeassistant.components import usb as usb
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_NAME as CONF_NAME
from homeassistant.helpers.service_info.usb import UsbServiceInfo as UsbServiceInfo
from serial.tools.list_ports_common import ListPortInfo as ListPortInfo
from typing import Any

DATA_SCHEMA: Incomplete

def _generate_unique_id(port: ListPortInfo) -> str: ...

class PhoneModemFlowHandler(ConfigFlow, domain=DOMAIN):
    _device: str | None
    def __init__(self) -> None: ...
    async def async_step_usb(self, discovery_info: UsbServiceInfo) -> ConfigFlowResult: ...
    async def async_step_usb_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def validate_device_errors(self, dev_path: str, unique_id: str) -> dict[str, str] | None: ...
