import openai
from .api import async_create_client as async_create_client, async_list_models as async_list_models
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError

_LOGGER: Incomplete
PLATFORMS: Incomplete
type LlamaCppConfigEntry = ConfigEntry[openai.AsyncOpenAI]

async def async_setup_entry(hass: HomeAssistant, entry: LlamaCppConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LlamaCppConfigEntry) -> bool: ...
async def async_update_options(hass: HomeAssistant, entry: LlamaCppConfigEntry) -> None: ...
