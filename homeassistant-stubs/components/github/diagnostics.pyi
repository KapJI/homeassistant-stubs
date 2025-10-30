from .coordinator import GithubConfigEntry as GithubConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import SERVER_SOFTWARE as SERVER_SOFTWARE, async_get_clientsession as async_get_clientsession
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: GithubConfigEntry) -> dict[str, Any]: ...
