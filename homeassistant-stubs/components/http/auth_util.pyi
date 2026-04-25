from aiohttp.web import Request as Request
from homeassistant.auth.models import User as User
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.http import current_request as current_request
from homeassistant.helpers.network import is_cloud_connection as is_cloud_connection
from homeassistant.util.network import is_local as is_local

@callback
def async_user_not_allowed_do_auth(hass: HomeAssistant, user: User, request: Request | None = None) -> str | None: ...
