from .const import CONF_NEW_TOKEN as CONF_NEW_TOKEN, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_CODE as CONF_CODE, CONF_NAME as CONF_NAME, CONF_TOKEN as CONF_TOKEN
from homeassistant.helpers.selector import BooleanSelector as BooleanSelector, BooleanSelectorConfig as BooleanSelectorConfig, QrCodeSelector as QrCodeSelector, QrCodeSelectorConfig as QrCodeSelectorConfig, QrErrorCorrectionLevel as QrErrorCorrectionLevel
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
STEP_CONFIRM_DATA_SCHEMA: Incomplete

class TOTPConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    user_input: dict[str, Any]
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
