from .const import DEFAULT_HOST as DEFAULT_HOST, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers import selector as selector
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from sfrbox_api.bridge import SFRBox
from typing import Any

_LOGGER: Incomplete
DATA_SCHEMA: Incomplete
AUTH_SCHEMA: Incomplete

class SFRBoxFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _box: SFRBox
    _config: dict[str, Any]
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_choose_auth(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_auth(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_skip_auth(self, user_input: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: Mapping[str, Any]) -> ConfigFlowResult: ...
