import openai
from .const import CONF_CHAT_MODEL as CONF_CHAT_MODEL, CONF_FILENAMES as CONF_FILENAMES, CONF_MAX_TOKENS as CONF_MAX_TOKENS, CONF_PROMPT as CONF_PROMPT, CONF_REASONING_EFFORT as CONF_REASONING_EFFORT, CONF_TEMPERATURE as CONF_TEMPERATURE, CONF_TOP_P as CONF_TOP_P, DOMAIN as DOMAIN, LOGGER as LOGGER, RECOMMENDED_CHAT_MODEL as RECOMMENDED_CHAT_MODEL, RECOMMENDED_MAX_TOKENS as RECOMMENDED_MAX_TOKENS, RECOMMENDED_REASONING_EFFORT as RECOMMENDED_REASONING_EFFORT, RECOMMENDED_TEMPERATURE as RECOMMENDED_TEMPERATURE, RECOMMENDED_TOP_P as RECOMMENDED_TOP_P
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.typing import ConfigType as ConfigType
from openai.types.images_response import ImagesResponse as ImagesResponse
from openai.types.responses import Response as Response, ResponseInputMessageContentListParam as ResponseInputMessageContentListParam, ResponseInputParam as ResponseInputParam

SERVICE_GENERATE_IMAGE: str
SERVICE_GENERATE_CONTENT: str
PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
type OpenAIConfigEntry = ConfigEntry[openai.AsyncClient]

def encode_file(file_path: str) -> tuple[str, str]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: OpenAIConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
