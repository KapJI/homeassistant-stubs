from .const import BASE_URL as BASE_URL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from openai import AsyncOpenAI

PLATFORMS: Incomplete
type OVHcloudAIEndpointsConfigEntry = ConfigEntry[AsyncOpenAI]

def _create_client(hass: HomeAssistant, api_key: str) -> AsyncOpenAI: ...
async def _validate_api_key(client: AsyncOpenAI) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: OVHcloudAIEndpointsConfigEntry) -> bool: ...
async def async_update_entry(hass: HomeAssistant, entry: OVHcloudAIEndpointsConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: OVHcloudAIEndpointsConfigEntry) -> bool: ...
