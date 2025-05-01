import contextvars
from collections.abc import Generator
from contextlib import contextmanager
from homeassistant.components.application_credentials import AuthorizationServer as AuthorizationServer
from homeassistant.core import HomeAssistant as HomeAssistant

CONF_ACTIVE_AUTHORIZATION_SERVER: str
_mcp_context: contextvars.ContextVar[AuthorizationServer]

@contextmanager
def authorization_server_context(authorization_server: AuthorizationServer) -> Generator[None]: ...
async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer: ...
