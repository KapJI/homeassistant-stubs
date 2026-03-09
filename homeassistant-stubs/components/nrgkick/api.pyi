from .const import DOMAIN as DOMAIN
from collections.abc import Awaitable
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

class NRGkickApiClientInvalidResponseError(NRGkickApiClientError):
    translation_domain = DOMAIN
    translation_key: str

async def async_api_call[_T](awaitable: Awaitable[_T]) -> _T: ...
