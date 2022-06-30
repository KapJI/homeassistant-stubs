from .const import CONF_FROM as CONF_FROM, CONF_TIME as CONF_TIME, CONF_TO as CONF_TO, DOMAIN as DOMAIN
from .util import create_unique_id as create_unique_id
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_NAME as CONF_NAME, CONF_WEEKDAY as CONF_WEEKDAY, WEEKDAYS as WEEKDAYS
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

ERROR_INVALID_AUTH: str
ERROR_INVALID_STATION: str
ERROR_MULTIPLE_STATION: str
DATA_SCHEMA: Incomplete
DATA_SCHEMA_REAUTH: Incomplete

class TVTrainConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    entry: Union[config_entries.ConfigEntry, None]
    async def validate_input(self, api_key: str, train_from: str, train_to: str) -> None: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
