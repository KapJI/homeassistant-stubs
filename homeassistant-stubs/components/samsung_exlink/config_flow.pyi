from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_MODEL as CONF_MODEL
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, SerialPortSelector as SerialPortSelector
from samsung_exlink import TVModel as TVModel
from typing import Any, override

DATA_SCHEMA: Incomplete
RESULT_NO_TV: str

async def _async_attempt_connect(port: str, model: TVModel | None) -> str | None: ...

class SamsungExLinkConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _user_input: dict[str, Any] | None
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_troubleshoot(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
