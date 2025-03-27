from .const import ATTR_DATE as ATTR_DATE, ATTR_NUSACH as ATTR_NUSACH, DOMAIN as DOMAIN, SERVICE_COUNT_OMER as SERVICE_COUNT_OMER
from _typeshed import Incomplete
from homeassistant.const import CONF_LANGUAGE as CONF_LANGUAGE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.helpers.selector import LanguageSelector as LanguageSelector, LanguageSelectorConfig as LanguageSelectorConfig

SUPPORTED_LANGUAGES: Incomplete
OMER_SCHEMA: Incomplete

def async_setup_services(hass: HomeAssistant) -> None: ...
