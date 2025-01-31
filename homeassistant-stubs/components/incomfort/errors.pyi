from .const import DOMAIN as DOMAIN
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError

class NotFound(HomeAssistantError):
    translation_domain = DOMAIN
    translation_key: str

class NoHeaters(ConfigEntryNotReady):
    translation_domain = DOMAIN
    translation_key: str

class InComfortTimeout(ConfigEntryNotReady):
    translation_domain = DOMAIN
    translation_key: str

class InComfortUnknownError(ConfigEntryNotReady):
    translation_domain = DOMAIN
    translation_key: str
