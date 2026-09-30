from .const import CONF_UNIT_ID as CONF_UNIT_ID, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_UNIT_ID as DEFAULT_UNIT_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.modbus import async_get_temporary_unit as async_get_temporary_unit
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, TextSelector as TextSelector
from sofar_modbus.modern.device import SofarInverter
from typing import Any, override

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def _async_probe(hass: HomeAssistant, host: str, port: int, unit_id: int) -> SofarInverter: ...

class SofarConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
