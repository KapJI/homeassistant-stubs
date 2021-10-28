from .const import CONF_APPTOKEN as CONF_APPTOKEN, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Any

class EfergyFlowHandler(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_import(self, import_config: ConfigType) -> FlowResult: ...
    async def async_step_reauth(self, config: dict[str, Any]) -> FlowResult: ...
    async def _async_try_connect(self, api_key: str) -> tuple[Union[str, None], Union[str, None]]: ...
