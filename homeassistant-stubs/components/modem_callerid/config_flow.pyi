from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, EXCEPTIONS as EXCEPTIONS
from homeassistant import config_entries as config_entries
from homeassistant.components import usb as usb
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_NAME as CONF_NAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from serial.tools.list_ports_common import ListPortInfo as ListPortInfo
from typing import Any

_LOGGER: Any
DATA_SCHEMA: Any

def _generate_unique_id(port: ListPortInfo) -> str: ...

class PhoneModemFlowHandler(config_entries.ConfigFlow):
    _device: Any
    def __init__(self) -> None: ...
    async def async_step_usb(self, discovery_info: dict[str, str]) -> FlowResult: ...
    async def async_step_usb_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, config: dict[str, Any]) -> FlowResult: ...
    async def validate_device_errors(self, dev_path: str, unique_id: str) -> Union[dict[str, str], None]: ...