from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from pyHomee import Homee
from typing import Any

_LOGGER: Incomplete
AUTH_SCHEMA: Incomplete

class HomeeConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    homee: Homee
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
