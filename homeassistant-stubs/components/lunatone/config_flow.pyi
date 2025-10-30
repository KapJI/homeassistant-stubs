import voluptuous as vol
from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any, Final

DATA_SCHEMA: Final[vol.Schema]

def compose_title(name: str | None, serial_number: int) -> str: ...

class LunatoneConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
