from .const import DOMAIN as DOMAIN, ZHA_HW_DISCOVERY_DATA as ZHA_HW_DISCOVERY_DATA
from homeassistant.components.homeassistant_hardware import silabs_multiprotocol_addon as silabs_multiprotocol_addon
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

class HomeAssistantYellowConfigFlow(ConfigFlow):
    VERSION: int
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> HomeAssistantYellowOptionsFlow: ...
    async def async_step_system(self, data: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class HomeAssistantYellowOptionsFlow(silabs_multiprotocol_addon.OptionsFlowHandler):
    async def _async_serial_port_settings(self) -> silabs_multiprotocol_addon.SerialPortSettings: ...
    async def _async_zha_physical_discovery(self) -> dict[str, Any]: ...
    def _zha_name(self) -> str: ...
    def _hardware_name(self) -> str: ...