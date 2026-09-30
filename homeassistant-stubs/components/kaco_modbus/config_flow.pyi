from .const import CONF_UNIT_ID as CONF_UNIT_ID, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_UNIT_ID as DEFAULT_UNIT_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.modbus import async_get_temporary_unit as async_get_temporary_unit
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, TextSelector as TextSelector
from typing import Any, override

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

class KacoModbusConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
