from .const import CONF_LANGUAGE_CODE as CONF_LANGUAGE_CODE, DOMAIN as DOMAIN, SUPPORTED_LANGUAGE_CODES as SUPPORTED_LANGUAGE_CODES
from .helpers import GoogleAssistantSDKAudioView as GoogleAssistantSDKAudioView, GoogleAssistantSDKConfigEntry as GoogleAssistantSDKConfigEntry, GoogleAssistantSDKRuntimeData as GoogleAssistantSDKRuntimeData, InMemoryStorage as InMemoryStorage, best_matching_language_code as best_matching_language_code
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from gassist_text import TextAssistant
from homeassistant.components import conversation as conversation
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery, intent as intent
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: GoogleAssistantSDKConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: GoogleAssistantSDKConfigEntry) -> bool: ...

class GoogleAssistantConversationAgent(conversation.AbstractConversationAgent):
    hass: Incomplete
    entry: Incomplete
    assistant: TextAssistant | None
    session: OAuth2Session | None
    language: str | None
    def __init__(self, hass: HomeAssistant, entry: GoogleAssistantSDKConfigEntry) -> None: ...
    @property
    def supported_languages(self) -> list[str]: ...
    async def async_process(self, user_input: conversation.ConversationInput) -> conversation.ConversationResult: ...
