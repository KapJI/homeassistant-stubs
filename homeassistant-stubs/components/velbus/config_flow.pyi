from .const import CONF_TLS as CONF_TLS, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT
from homeassistant.helpers.service_info.usb import UsbServiceInfo as UsbServiceInfo
from typing import Any

class VelbusConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    _errors: dict[str, str]
    _device: str
    _title: str
    def __init__(self) -> None: ...
    def _create_device(self) -> ConfigFlowResult: ...
    async def _test_connection(self) -> bool: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_network(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_usbselect(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_usb(self, discovery_info: UsbServiceInfo) -> ConfigFlowResult: ...
    async def async_step_discovery_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
