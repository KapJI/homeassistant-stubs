from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components import usb as usb
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.util import slugify as slugify
from typing import Any

class VelbusConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _errors: Incomplete
    _device: str
    _title: str
    def __init__(self) -> None: ...
    def _create_device(self, name: str, prt: str) -> FlowResult: ...
    async def _test_connection(self, prt: str) -> bool: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_usb(self, discovery_info: usb.UsbServiceInfo) -> FlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
