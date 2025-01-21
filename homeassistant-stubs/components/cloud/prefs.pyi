from .const import DEFAULT_ALEXA_REPORT_STATE as DEFAULT_ALEXA_REPORT_STATE, DEFAULT_EXPOSED_DOMAINS as DEFAULT_EXPOSED_DOMAINS, DEFAULT_GOOGLE_REPORT_STATE as DEFAULT_GOOGLE_REPORT_STATE, DEFAULT_TTS_DEFAULT_VOICE as DEFAULT_TTS_DEFAULT_VOICE, DOMAIN as DOMAIN, PREF_ALEXA_DEFAULT_EXPOSE as PREF_ALEXA_DEFAULT_EXPOSE, PREF_ALEXA_ENTITY_CONFIGS as PREF_ALEXA_ENTITY_CONFIGS, PREF_ALEXA_REPORT_STATE as PREF_ALEXA_REPORT_STATE, PREF_ALEXA_SETTINGS_VERSION as PREF_ALEXA_SETTINGS_VERSION, PREF_CLOUDHOOKS as PREF_CLOUDHOOKS, PREF_CLOUD_USER as PREF_CLOUD_USER, PREF_ENABLE_ALEXA as PREF_ENABLE_ALEXA, PREF_ENABLE_CLOUD_ICE_SERVERS as PREF_ENABLE_CLOUD_ICE_SERVERS, PREF_ENABLE_GOOGLE as PREF_ENABLE_GOOGLE, PREF_ENABLE_REMOTE as PREF_ENABLE_REMOTE, PREF_GOOGLE_CONNECTED as PREF_GOOGLE_CONNECTED, PREF_GOOGLE_DEFAULT_EXPOSE as PREF_GOOGLE_DEFAULT_EXPOSE, PREF_GOOGLE_ENTITY_CONFIGS as PREF_GOOGLE_ENTITY_CONFIGS, PREF_GOOGLE_LOCAL_WEBHOOK_ID as PREF_GOOGLE_LOCAL_WEBHOOK_ID, PREF_GOOGLE_REPORT_STATE as PREF_GOOGLE_REPORT_STATE, PREF_GOOGLE_SECURE_DEVICES_PIN as PREF_GOOGLE_SECURE_DEVICES_PIN, PREF_GOOGLE_SETTINGS_VERSION as PREF_GOOGLE_SETTINGS_VERSION, PREF_INSTANCE_ID as PREF_INSTANCE_ID, PREF_REMOTE_ALLOW_REMOTE_ENABLE as PREF_REMOTE_ALLOW_REMOTE_ENABLE, PREF_REMOTE_DOMAIN as PREF_REMOTE_DOMAIN, PREF_TTS_DEFAULT_VOICE as PREF_TTS_DEFAULT_VOICE, PREF_USERNAME as PREF_USERNAME
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.auth.const import GROUP_ID_ADMIN as GROUP_ID_ADMIN
from homeassistant.auth.models import User as User
from homeassistant.components import webhook as webhook
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.util.logging import async_create_catching_coro as async_create_catching_coro
from typing import Any

STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
STORAGE_VERSION_MINOR: int
ALEXA_SETTINGS_VERSION: int
GOOGLE_SETTINGS_VERSION: int

class CloudPreferencesStore(Store):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...

class CloudPreferences:
    _prefs: dict[str, Any]
    _hass: Incomplete
    _store: Incomplete
    _listeners: list[Callable[[CloudPreferences], Coroutine[Any, Any, None]]]
    last_updated: set[str]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_initialize(self) -> None: ...
    @callback
    def async_listen_updates(self, listener: Callable[[CloudPreferences], Coroutine[Any, Any, None]]) -> Callable[[], None]: ...
    async def async_update(self, *, alexa_enabled: bool | UndefinedType = ..., alexa_report_state: bool | UndefinedType = ..., alexa_settings_version: int | UndefinedType = ..., cloud_ice_servers_enabled: bool | UndefinedType = ..., cloud_user: str | UndefinedType = ..., cloudhooks: dict[str, dict[str, str | bool]] | UndefinedType = ..., google_connected: bool | UndefinedType = ..., google_enabled: bool | UndefinedType = ..., google_report_state: bool | UndefinedType = ..., google_secure_devices_pin: str | None | UndefinedType = ..., google_settings_version: int | UndefinedType = ..., remote_allow_remote_enable: bool | UndefinedType = ..., remote_domain: str | None | UndefinedType = ..., remote_enabled: bool | UndefinedType = ..., tts_default_voice: tuple[str, str] | UndefinedType = ...) -> None: ...
    async def async_set_username(self, username: str | None) -> bool: ...
    async def async_erase_config(self) -> None: ...
    def as_dict(self) -> dict[str, Any]: ...
    @property
    def remote_allow_remote_enable(self) -> bool: ...
    @property
    def remote_enabled(self) -> bool: ...
    @property
    def remote_domain(self) -> str | None: ...
    @property
    def alexa_enabled(self) -> bool: ...
    @property
    def alexa_report_state(self) -> bool: ...
    @property
    def alexa_default_expose(self) -> list[str] | None: ...
    @property
    def alexa_entity_configs(self) -> dict[str, Any]: ...
    @property
    def alexa_settings_version(self) -> int: ...
    @property
    def google_enabled(self) -> bool: ...
    @property
    def google_connected(self) -> bool: ...
    @property
    def google_report_state(self) -> bool: ...
    @property
    def google_secure_devices_pin(self) -> str | None: ...
    @property
    def google_entity_configs(self) -> dict[str, dict[str, Any]]: ...
    @property
    def google_settings_version(self) -> int: ...
    @property
    def google_local_webhook_id(self) -> str: ...
    @property
    def google_default_expose(self) -> list[str] | None: ...
    @property
    def cloudhooks(self) -> dict[str, Any]: ...
    @property
    def instance_id(self) -> str | None: ...
    @property
    def tts_default_voice(self) -> tuple[str, str]: ...
    @property
    def cloud_ice_servers_enabled(self) -> bool: ...
    async def get_cloud_user(self) -> str: ...
    async def _load_cloud_user(self) -> User | None: ...
    async def _save_prefs(self, prefs: dict[str, Any]) -> None: ...
    @callback
    @staticmethod
    def _empty_config(username: str) -> dict[str, Any]: ...
