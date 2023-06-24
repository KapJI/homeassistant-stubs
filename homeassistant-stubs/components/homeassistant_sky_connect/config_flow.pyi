from .const import DOMAIN as DOMAIN
from .util import get_usb_service_info as get_usb_service_info
from homeassistant.components import usb as usb
from homeassistant.components.homeassistant_hardware import silabs_multiprotocol_addon as silabs_multiprotocol_addon
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class HomeAssistantSkyConnectConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> HomeAssistantSkyConnectOptionsFlow: ...
    async def async_step_usb(self, discovery_info: usb.UsbServiceInfo) -> FlowResult: ...

class HomeAssistantSkyConnectOptionsFlow(silabs_multiprotocol_addon.OptionsFlowHandler):
    async def _async_serial_port_settings(self) -> silabs_multiprotocol_addon.SerialPortSettings: ...
    async def _async_zha_physical_discovery(self) -> dict[str, Any]: ...
    def _zha_name(self) -> str: ...
    def _hardware_name(self) -> str: ...
