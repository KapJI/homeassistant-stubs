import voluptuous as vol
from . import MULTI_FACTOR_AUTH_MODULES as MULTI_FACTOR_AUTH_MODULES, MULTI_FACTOR_AUTH_MODULE_SCHEMA as MULTI_FACTOR_AUTH_MODULE_SCHEMA, MultiFactorAuthModule as MultiFactorAuthModule, SetupFlow as SetupFlow
from _typeshed import Incomplete
from homeassistant.const import CONF_EXCLUDE as CONF_EXCLUDE, CONF_INCLUDE as CONF_INCLUDE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.exceptions import ServiceNotFound as ServiceNotFound
from homeassistant.helpers.storage import Store as Store
from typing import Any

REQUIREMENTS: Incomplete
CONF_MESSAGE: str
CONFIG_SCHEMA: Incomplete
STORAGE_VERSION: int
STORAGE_KEY: str
STORAGE_USERS: str
STORAGE_USER_ID: str
INPUT_FIELD_CODE: str
_LOGGER: Incomplete

def _generate_secret() -> str: ...
def _generate_random() -> int: ...
def _generate_otp(secret: str, count: int) -> str: ...
def _verify_otp(secret: str, otp: str, count: int) -> bool: ...

class NotifySetting:
    secret: str
    counter: int
    notify_service: str | None
    target: str | None
    def __init__(self, secret, counter, notify_service, target) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
type _UsersDict = dict[str, NotifySetting]

class NotifyAuthModule(MultiFactorAuthModule):
    DEFAULT_TITLE: str
    _user_settings: _UsersDict | None
    _user_store: Incomplete
    _include: Incomplete
    _exclude: Incomplete
    _message_template: Incomplete
    _init_lock: Incomplete
    def __init__(self, hass: HomeAssistant, config: dict[str, Any]) -> None: ...
    @property
    def input_schema(self) -> vol.Schema: ...
    async def _async_load(self) -> None: ...
    async def _async_save(self) -> None: ...
    @callback
    def aync_get_available_notify_services(self) -> list[str]: ...
    async def async_setup_flow(self, user_id: str) -> NotifySetupFlow: ...
    async def async_setup_user(self, user_id: str, setup_data: Any) -> Any: ...
    async def async_depose_user(self, user_id: str) -> None: ...
    async def async_is_user_setup(self, user_id: str) -> bool: ...
    async def async_validate(self, user_id: str, user_input: dict[str, Any]) -> bool: ...
    async def async_initialize_login_mfa_step(self, user_id: str) -> None: ...
    async def async_notify_user(self, user_id: str, code: str) -> None: ...
    async def async_notify(self, code: str, notify_service: str, target: str | None = None) -> None: ...

class NotifySetupFlow(SetupFlow[NotifyAuthModule]):
    _available_notify_services: Incomplete
    _secret: str | None
    _count: int | None
    _notify_service: str | None
    _target: str | None
    def __init__(self, auth_module: NotifyAuthModule, setup_schema: vol.Schema, user_id: str, available_notify_services: list[str]) -> None: ...
    async def async_step_init(self, user_input: dict[str, str] | None = None) -> FlowResult: ...
    async def async_step_setup(self, user_input: dict[str, str] | None = None) -> FlowResult: ...
