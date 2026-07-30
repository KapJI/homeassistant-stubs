from .const import CONF_BASE_URL as CONF_BASE_URL, CONF_CORS_ORIGINS as CONF_CORS_ORIGINS, CONF_IP_BAN_ENABLED as CONF_IP_BAN_ENABLED, CONF_LOGIN_ATTEMPTS_THRESHOLD as CONF_LOGIN_ATTEMPTS_THRESHOLD, CONF_SERVER_HOST as CONF_SERVER_HOST, CONF_SERVER_PORT as CONF_SERVER_PORT, CONF_SSL_CERTIFICATE as CONF_SSL_CERTIFICATE, CONF_SSL_KEY as CONF_SSL_KEY, CONF_SSL_PEER_CERTIFICATE as CONF_SSL_PEER_CERTIFICATE, CONF_SSL_PROFILE as CONF_SSL_PROFILE, CONF_TRUSTED_PROXIES as CONF_TRUSTED_PROXIES, CONF_USE_X_FORWARDED_FOR as CONF_USE_X_FORWARDED_FOR, CONF_USE_X_FRAME_OPTIONS as CONF_USE_X_FRAME_OPTIONS, DEFAULT_CORS as DEFAULT_CORS, DOMAIN as DOMAIN, ENV_SETUP_PORT as ENV_SETUP_PORT, ENV_SUPERVISOR as ENV_SUPERVISOR, NO_LOGIN_ATTEMPT_THRESHOLD as NO_LOGIN_ATTEMPT_THRESHOLD, SSL_INTERMEDIATE as SSL_INTERMEDIATE, SSL_MODERN as SSL_MODERN, SUPERVISOR_DEFAULT_PORT as SUPERVISOR_DEFAULT_PORT
from _typeshed import Incomplete
from datetime import datetime
from enum import StrEnum
from homeassistant.const import SERVER_PORT as SERVER_PORT
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Final, TypedDict, override

_LOGGER: Incomplete

def default_server_port() -> int: ...

STORAGE_KEY: Final[Incomplete]
STORAGE_VERSION: Final[int]
STORAGE_MINOR_VERSION: Final[int]
KEY_STABLE: Final[str]
KEY_PENDING: Final[str]
KEY_YAML_MIGRATION_DONE: Final[str]
AUTO_REVERT_DELAY: Final[Incomplete]
HTTP_CONFIG_CREATED_AT: Final[str]
HTTP_CONFIG_ERROR: Final[str]
HTTP_CONFIG_ERROR_MESSAGE: Final[str]
ERROR_APPLY_FAILED: Final[str]
ERROR_NOT_PROMOTED: Final[str]
DATA_STORE: HassKey[HTTPConfigStore]

class ConfData(TypedDict, total=False):
    server_host: list[str]
    server_port: int
    ssl_certificate: str
    ssl_peer_certificate: str
    ssl_key: str
    cors_allowed_origins: list[str]
    use_x_forwarded_for: bool
    trusted_proxies: list[str]
    login_attempts_threshold: int
    ip_ban_enabled: bool
    ssl_profile: str
    use_x_frame_options: bool
    created_at: str
    error: str | None
    error_message: str | None

class ActiveConfigType(StrEnum):
    STABLE = 'stable'
    PENDING = 'pending'
    DEFAULT = 'default'
    DEFAULT_LEGACY_PORT = 'default_legacy_port'

class _HTTPStoreData(TypedDict):
    stable: ConfData
    pending: ConfData | None
    yaml_migration_done: bool

def _ip_network_str(value: Any) -> str: ...

HTTP_STORAGE_SCHEMA: Final[Incomplete]
_DEFAULT_CONFIG: Final[ConfData]
_META_KEYS: Final[Incomplete]

def _strip_meta(config: ConfData) -> ConfData: ...

_DEFAULT_CONFIG_LEGACY_PORT: Final[ConfData]

async def async_load_config(hass: HomeAssistant, config: ConfigType) -> ConfData: ...
async def async_get_and_load_store(hass: HomeAssistant) -> HTTPConfigStore: ...

class HTTPConfigStore:
    _hass: Incomplete
    _store: Incomplete
    _stable: ConfData
    _pending: ConfData | None
    _active_config_type: ActiveConfigType
    _yaml_migration_done: bool
    _loaded: bool
    _load_lock: Incomplete
    _revert_unsub: CALLBACK_TYPE | None
    _revert_deadline: datetime | None
    def __init__(self, hass: HomeAssistant) -> None: ...
    @property
    def stable(self) -> ConfData: ...
    @property
    def pending(self) -> ConfData | None: ...
    @property
    def default(self) -> ConfData: ...
    @property
    def active_config_type(self) -> ActiveConfigType: ...
    @property
    def revert_deadline(self) -> datetime | None: ...
    @property
    def yaml_migration_done(self) -> bool: ...
    async def async_load(self) -> None: ...
    async def async_set_pending(self, config: ConfData | None) -> None: ...
    async def async_promote_pending(self) -> None: ...
    @callback
    def async_schedule_revert_to_stable(self) -> None: ...
    @callback
    def async_cancel_revert(self) -> None: ...
    async def _async_revert_to_stable(self, _now: datetime) -> None: ...
    async def async_mark_yaml_migration_done(self) -> None: ...
    async def async_migrate_yaml(self, config: ConfData) -> None: ...
    def _stable_differs_only_by_lost_proxy_masks(self, config: ConfData) -> bool: ...
    async def _async_persist(self) -> None: ...
    async def async_activate_config(self) -> ConfData: ...
    async def async_get_fallback_config(self, err: HomeAssistantError | OSError) -> ConfData: ...

class _HTTPStore(Store[_HTTPStoreData]):
    @override
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...
