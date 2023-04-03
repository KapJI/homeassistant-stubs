from . import AUTH_PROVIDERS as AUTH_PROVIDERS, AUTH_PROVIDER_SCHEMA as AUTH_PROVIDER_SCHEMA, AuthProvider as AuthProvider, LoginFlow as LoginFlow
from ..models import Credentials as Credentials, UserMeta as UserMeta
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

AUTH_PROVIDER_TYPE: str
CONF_API_PASSWORD: str
CONFIG_SCHEMA: Incomplete
LEGACY_USER_NAME: str

class InvalidAuthError(HomeAssistantError): ...

class LegacyApiPasswordAuthProvider(AuthProvider):
    DEFAULT_TITLE: str
    @property
    def api_password(self) -> str: ...
    async def async_login_flow(self, context: dict[str, Any] | None) -> LoginFlow: ...
    def async_validate_login(self, password: str) -> None: ...
    async def async_get_or_create_credentials(self, flow_result: Mapping[str, str]) -> Credentials: ...
    async def async_user_meta_for_credentials(self, credentials: Credentials) -> UserMeta: ...

class LegacyLoginFlow(LoginFlow):
    async def async_step_init(self, user_input: dict[str, str] | None = ...) -> FlowResult: ...
