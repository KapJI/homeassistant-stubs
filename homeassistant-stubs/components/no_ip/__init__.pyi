import aiohttp
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, CONF_PASSWORD as CONF_PASSWORD, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import SERVER_SOFTWARE as SERVER_SOFTWARE
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Any
DOMAIN: str
EMAIL: str
INTERVAL: Any
DEFAULT_TIMEOUT: int
NO_IP_ERRORS: Any
UPDATE_URL: str
HA_USER_AGENT: Any
CONFIG_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _update_no_ip(hass: HomeAssistant, session: aiohttp.ClientSession, domain: str, auth_str: bytes, timeout: int) -> bool: ...
