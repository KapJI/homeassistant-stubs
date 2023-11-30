from . import AUTH_PROVIDERS as AUTH_PROVIDERS, AUTH_PROVIDER_SCHEMA as AUTH_PROVIDER_SCHEMA, AuthProvider as AuthProvider, LoginFlow as LoginFlow
from ..models import Credentials as Credentials, UserMeta as UserMeta
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.core import async_get_hass as async_get_hass, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from typing import Any

AUTH_PROVIDER_TYPE: str
CONF_API_PASSWORD: str
_CONFIG_SCHEMA: Incomplete

def _create_repair_and_validate(config: dict[str, Any]) -> dict[str, Any]: ...
CONFIG_SCHEMA = _create_repair_and_validate
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
