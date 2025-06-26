from .const import ATTR_AFTER_SUNSET as ATTR_AFTER_SUNSET, ATTR_DATE as ATTR_DATE, ATTR_NUSACH as ATTR_NUSACH, DOMAIN as DOMAIN, SERVICE_COUNT_OMER as SERVICE_COUNT_OMER
from _typeshed import Incomplete
from homeassistant.const import CONF_LANGUAGE as CONF_LANGUAGE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.selector import LanguageSelector as LanguageSelector, LanguageSelectorConfig as LanguageSelectorConfig
from homeassistant.helpers.sun import get_astral_event_date as get_astral_event_date

_LOGGER: Incomplete
OMER_SCHEMA: Incomplete

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
