from .const import CONF_CALENDAR_NAME as CONF_CALENDAR_NAME, DOMAIN as DOMAIN
from .ics import InvalidIcsException as InvalidIcsException, parse_calendar as parse_calendar
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

class RemoteCalendarConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
