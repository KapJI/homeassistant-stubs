from .const import CONF_TENANT_ID as CONF_TENANT_ID, DOMAIN as DOMAIN, OAUTH2_AUTHORIZE as OAUTH2_AUTHORIZE, OAUTH2_TOKEN as OAUTH2_TOKEN
from collections.abc import Generator
from contextlib import contextmanager
from contextvars import ContextVar
from homeassistant.components.application_credentials import AuthorizationServer as AuthorizationServer
from homeassistant.core import HomeAssistant as HomeAssistant

_tenant_id_context: ContextVar[str]

@contextmanager
def tenant_id_context(tenant_id: str) -> Generator[None]: ...
async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer: ...
