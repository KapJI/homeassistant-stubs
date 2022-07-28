from .const import DOMAIN as DOMAIN
from .helpers import fetch_site as fetch_site
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries, core as core, exceptions as exceptions
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

_LOGGER: Incomplete

async def validate_input(hass: core.HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class MetOfficeConfigFlow(config_entries.ConfigFlow):
    VERSION: int
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...

class CannotConnect(exceptions.HomeAssistantError): ...
