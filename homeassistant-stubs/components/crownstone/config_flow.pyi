from .const import CONF_USB_MANUAL_PATH as CONF_USB_MANUAL_PATH, CONF_USB_PATH as CONF_USB_PATH, CONF_USB_SPHERE as CONF_USB_SPHERE, CONF_USB_SPHERE_OPTION as CONF_USB_SPHERE_OPTION, CONF_USE_USB_OPTION as CONF_USE_USB_OPTION, DOMAIN as DOMAIN, DONT_USE_USB as DONT_USE_USB, MANUAL_PATH as MANUAL_PATH, REFRESH_LIST as REFRESH_LIST
from .helpers import list_ports_as_str as list_ports_as_str
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from crownstone_cloud import CrownstoneCloud
from homeassistant.components import usb as usb
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowHandler as FlowHandler, FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client
from serial.tools.list_ports_common import ListPortInfo as ListPortInfo
from typing import Any

CONFIG_FLOW: str
OPTIONS_FLOW: str

class BaseCrownstoneFlowHandler(FlowHandler):
    cloud: CrownstoneCloud
    flow_type: Incomplete
    create_entry_callback: Incomplete
    usb_path: Incomplete
    usb_sphere_id: Incomplete
    def __init__(self, flow_type: str, create_entry_cb: Callable[..., FlowResult]) -> None: ...
    async def async_step_usb_config(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_usb_manual_config(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_usb_sphere_config(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class CrownstoneConfigFlowHandler(BaseCrownstoneFlowHandler, ConfigFlow):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> CrownstoneOptionsFlowHandler: ...
    login_info: Incomplete
    def __init__(self) -> None: ...
    cloud: Incomplete
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    def async_create_new_entry(self) -> FlowResult: ...

class CrownstoneOptionsFlowHandler(BaseCrownstoneFlowHandler, OptionsFlow):
    entry: Incomplete
    updated_options: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    cloud: Incomplete
    async def async_step_init(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    def async_create_new_entry(self) -> FlowResult: ...
