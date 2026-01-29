from .const import DOMAIN as DOMAIN
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

class NRGkickApiClientError(HomeAssistantError):
    translation_domain = DOMAIN
    translation_key: str

class NRGkickApiClientCommunicationError(NRGkickApiClientError):
    translation_domain = DOMAIN
    translation_key: str

class NRGkickApiClientAuthenticationError(NRGkickApiClientError):
    translation_domain = DOMAIN
    translation_key: str

class NRGkickApiClientApiDisabledError(NRGkickApiClientError):
    translation_domain = DOMAIN
    translation_key: str

class NRGkickApiClientInvalidResponseError(NRGkickApiClientError): ...
