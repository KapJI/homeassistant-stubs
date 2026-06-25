from .const import CONF_SET_ID as CONF_SET_ID, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE as CONF_DEVICE
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, SerialPortSelector as SerialPortSelector
from typing import Any, override

DATA_SCHEMA: Incomplete
RESULT_NO_TV: str

async def _async_attempt_connect(port: str, set_id: int) -> str | None: ...

class LGTVRS232ConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _user_input: dict[str, Any] | None
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_troubleshoot(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
