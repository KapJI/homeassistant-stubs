from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from openai import AsyncOpenAI

PLATFORMS: Incomplete
type OpenRouterConfigEntry = ConfigEntry[AsyncOpenAI]

async def async_setup_entry(hass: HomeAssistant, entry: OpenRouterConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: OpenRouterConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: OpenRouterConfigEntry) -> bool: ...
