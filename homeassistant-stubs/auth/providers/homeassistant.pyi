from . import AUTH_PROVIDERS as AUTH_PROVIDERS, AUTH_PROVIDER_SCHEMA as AUTH_PROVIDER_SCHEMA, AuthProvider as AuthProvider, LoginFlow as LoginFlow
from ..models import AuthFlowContext as AuthFlowContext, AuthFlowResult as AuthFlowResult, Credentials as Credentials, UserMeta as UserMeta
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.storage import Store as Store
from typing import Any

STORAGE_VERSION: int
STORAGE_KEY: str

def _disallow_id(conf: dict[str, Any]) -> dict[str, Any]: ...

CONFIG_SCHEMA: Incomplete

@callback
def async_get_provider(hass: HomeAssistant) -> HassAuthProvider: ...

class InvalidAuth(HomeAssistantError): ...

class InvalidUser(HomeAssistantError):
    def __init__(self, *args: object, translation_key: str | None = None, translation_placeholders: dict[str, str] | None = None) -> None: ...

class InvalidUsername(InvalidUser): ...

class Data:
    hass: Incomplete
    _store: Incomplete
    _data: dict[str, list[dict[str, str]]] | None
    is_legacy: bool
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def normalize_username(self, username: str, *, force_normalize: bool = False) -> str: ...
    async def async_load(self) -> None: ...
    @callback
    def _async_check_for_not_normalized_usernames(self, data: dict[str, list[dict[str, str]]]) -> None: ...
    @property
    def users(self) -> list[dict[str, str]]: ...
    def validate_login(self, username: str, password: str) -> None: ...
    def hash_password(self, password: str, for_storage: bool = False) -> bytes: ...
    def add_auth(self, username: str, password: str) -> None: ...
    @callback
    def async_remove_auth(self, username: str) -> None: ...
    def change_password(self, username: str, new_password: str) -> None: ...
    @callback
    def _validate_new_username(self, new_username: str) -> None: ...
    @callback
    def change_username(self, username: str, new_username: str) -> None: ...
    async def async_save(self) -> None: ...

class HassAuthProvider(AuthProvider):
    DEFAULT_TITLE: str
    data: Data | None
    _init_lock: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    async def async_initialize(self) -> None: ...
    async def async_login_flow(self, context: AuthFlowContext | None) -> HassLoginFlow: ...
    async def async_validate_login(self, username: str, password: str) -> None: ...
    async def async_add_auth(self, username: str, password: str) -> None: ...
    async def async_remove_auth(self, username: str) -> None: ...
    async def async_change_password(self, username: str, new_password: str) -> None: ...
    async def async_change_username(self, credential: Credentials, new_username: str) -> None: ...
    async def async_get_or_create_credentials(self, flow_result: Mapping[str, str]) -> Credentials: ...
    async def async_user_meta_for_credentials(self, credentials: Credentials) -> UserMeta: ...
    async def async_will_remove_credentials(self, credentials: Credentials) -> None: ...

class HassLoginFlow(LoginFlow[HassAuthProvider]):
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> AuthFlowResult: ...
