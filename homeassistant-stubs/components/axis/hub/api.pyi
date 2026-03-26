import axis
from ..const import LOGGER as LOGGER
from ..errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from collections.abc import Mapping
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

async def get_axis_api(hass: HomeAssistant, config: Mapping[str, Any]) -> axis.AxisDevice: ...
