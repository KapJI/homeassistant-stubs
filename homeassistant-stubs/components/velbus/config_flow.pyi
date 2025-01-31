from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT
from homeassistant.helpers.service_info.usb import UsbServiceInfo as UsbServiceInfo
from homeassistant.util import slugify as slugify
from typing import Any

class VelbusConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _errors: dict[str, str]
    _device: str
    _title: str
    def __init__(self) -> None: ...
    def _create_device(self, name: str, prt: str) -> ConfigFlowResult: ...
    async def _test_connection(self, prt: str) -> bool: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_usb(self, discovery_info: UsbServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
