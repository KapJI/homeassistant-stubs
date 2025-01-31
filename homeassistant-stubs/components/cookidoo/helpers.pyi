from .coordinator import CookidooConfigEntry as CookidooConfigEntry
from cookidoo_api import Cookidoo
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_EMAIL as CONF_EMAIL, CONF_LANGUAGE as CONF_LANGUAGE, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

async def cookidoo_from_config_data(hass: HomeAssistant, data: dict[str, Any]) -> Cookidoo: ...
async def cookidoo_from_config_entry(hass: HomeAssistant, entry: CookidooConfigEntry) -> Cookidoo: ...
