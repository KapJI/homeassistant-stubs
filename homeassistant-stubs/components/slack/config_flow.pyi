from .const import CONF_DEFAULT_CHANNEL as CONF_DEFAULT_CHANNEL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import aiohttp_client as aiohttp_client

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

class SlackFlowHandler(config_entries.ConfigFlow):
    async def async_step_user(self, user_input: Union[dict[str, str], None] = ...) -> FlowResult: ...
    async def async_step_import(self, import_config: dict[str, str]) -> FlowResult: ...
    async def _async_try_connect(self, token: str) -> Union[tuple[str, None], tuple[None, dict[str, str]]]: ...
