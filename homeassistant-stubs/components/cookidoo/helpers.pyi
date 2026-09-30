from .coordinator import CookidooConfigEntry as CookidooConfigEntry
from collections.abc import Callable as Callable
from cookidoo_api import Cookidoo, CookidooAuthData
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_EMAIL as CONF_EMAIL, CONF_LANGUAGE as CONF_LANGUAGE, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from typing import Any

async def cookidoo_from_config_data(hass: HomeAssistant, data: dict[str, Any], on_auth_data_update: Callable[[CookidooAuthData], None] | None = None) -> Cookidoo: ...
async def cookidoo_from_config_entry(hass: HomeAssistant, entry: CookidooConfigEntry) -> Cookidoo: ...
