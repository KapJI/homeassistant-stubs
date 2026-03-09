import anthropic
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, DEFAULT_CONVERSATION_NAME as DEFAULT_CONVERSATION_NAME, DEPRECATED_MODELS as DEPRECATED_MODELS, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
type AnthropicConfigEntry = ConfigEntry[anthropic.AsyncClient]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: AnthropicConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AnthropicConfigEntry) -> bool: ...
async def async_update_options(hass: HomeAssistant, entry: AnthropicConfigEntry) -> None: ...
async def async_migrate_integration(hass: HomeAssistant) -> None: ...
async def async_migrate_entry(hass: HomeAssistant, entry: AnthropicConfigEntry) -> bool: ...
