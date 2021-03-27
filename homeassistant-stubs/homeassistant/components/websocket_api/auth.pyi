from .connection import ActiveConnection as ActiveConnection
from .error import Disconnect as Disconnect
from homeassistant.auth.models import RefreshToken as RefreshToken, User as User
from homeassistant.components.http.ban import process_success_login as process_success_login, process_wrong_login as process_wrong_login
from typing import Any

TYPE_AUTH: str
TYPE_AUTH_INVALID: str
TYPE_AUTH_OK: str
TYPE_AUTH_REQUIRED: str
AUTH_MESSAGE_SCHEMA: Any

def auth_ok_message(): ...
def auth_required_message(): ...
def auth_invalid_message(message: Any): ...

class AuthPhase:
    def __init__(self, logger: Any, hass: Any, send_message: Any, request: Any) -> None: ...
    async def async_handle(self, msg: Any): ...
