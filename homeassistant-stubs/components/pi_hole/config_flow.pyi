from . import Hole as Hole, api_by_version as api_by_version, determine_api_version as determine_api_version
from .const import DEFAULT_LOCATION as DEFAULT_LOCATION, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_SSL as DEFAULT_SSL, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_HOST as CONF_HOST, CONF_LOCATION as CONF_LOCATION, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from typing import Any

_LOGGER: Incomplete

class PiHoleFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _config: dict
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_try_connect(self) -> dict[str, str]: ...
