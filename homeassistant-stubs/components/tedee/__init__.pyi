from .const import DOMAIN as DOMAIN, NAME as NAME
from .coordinator import TedeeApiCoordinator as TedeeApiCoordinator
from _typeshed import Incomplete
from aiohttp.web import Request as Request, Response as Response
from collections.abc import Awaitable, Callable as Callable
from homeassistant.components.http import HomeAssistantView as HomeAssistantView
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_WEBHOOK_ID as CONF_WEBHOOK_ID, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.network import get_url as get_url

PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TedeeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def get_webhook_handler(coordinator: TedeeApiCoordinator) -> Callable[[HomeAssistant, str, Request], Awaitable[Response | None]]: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
