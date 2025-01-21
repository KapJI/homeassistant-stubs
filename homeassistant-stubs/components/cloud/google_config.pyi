from .client import CloudClient as CloudClient
from .const import CONF_ENTITY_CONFIG as CONF_ENTITY_CONFIG, CONF_FILTER as CONF_FILTER, DEFAULT_DISABLE_2FA as DEFAULT_DISABLE_2FA, PREF_DISABLE_2FA as PREF_DISABLE_2FA, PREF_SHOULD_EXPOSE as PREF_SHOULD_EXPOSE
from .prefs import CloudPreferences as CloudPreferences, GOOGLE_SETTINGS_VERSION as GOOGLE_SETTINGS_VERSION
from _typeshed import Incomplete
from hass_nabucasa import Cloud as Cloud
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.components.google_assistant.helpers import AbstractConfig as AbstractConfig
from homeassistant.components.homeassistant.exposed_entities import async_expose_entity as async_expose_entity, async_get_assistant_settings as async_get_assistant_settings, async_get_entity_settings as async_get_entity_settings, async_listen_entity_updates as async_listen_entity_updates, async_set_assistant_option as async_set_assistant_option, async_should_expose as async_should_expose
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import CLOUD_NEVER_EXPOSED_ENTITIES as CLOUD_NEVER_EXPOSED_ENTITIES
from homeassistant.core import CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import device_registry as dr, entity_registry as er, start as start
from homeassistant.helpers.entity import get_device_class as get_device_class
from homeassistant.helpers.entityfilter import EntityFilter as EntityFilter
from homeassistant.setup import async_setup_component as async_setup_component
from http import HTTPStatus
from typing import Any

_LOGGER: Incomplete
CLOUD_GOOGLE: Incomplete
SUPPORTED_DOMAINS: Incomplete
SUPPORTED_BINARY_SENSOR_DEVICE_CLASSES: Incomplete
SUPPORTED_SENSOR_DEVICE_CLASSES: Incomplete

def _supported_legacy(hass: HomeAssistant, entity_id: str) -> bool: ...

class CloudGoogleConfig(AbstractConfig):
    _config: Incomplete
    _user: Incomplete
    _prefs: Incomplete
    _cloud: Incomplete
    _sync_entities_lock: Incomplete
    def __init__(self, hass: HomeAssistant, config: dict[str, Any], cloud_user: str, prefs: CloudPreferences, cloud: Cloud[CloudClient]) -> None: ...
    @property
    def enabled(self) -> bool: ...
    @property
    def entity_config(self) -> dict[str, Any]: ...
    @property
    def secure_devices_pin(self) -> str | None: ...
    @property
    def should_report_state(self) -> bool: ...
    def get_local_webhook_id(self, agent_user_id: Any) -> str: ...
    def get_local_user_id(self, webhook_id: Any) -> str: ...
    @property
    def cloud_user(self) -> str: ...
    def _migrate_google_entity_settings_v1(self) -> None: ...
    async def async_initialize(self) -> None: ...
    def should_expose(self, state: State) -> bool: ...
    def _should_expose_legacy(self, entity_id: str) -> bool: ...
    def _should_expose_entity_id(self, entity_id: str) -> bool: ...
    @property
    def agent_user_id(self) -> str: ...
    @property
    def has_registered_user_agent(self) -> bool: ...
    def get_agent_user_id_from_context(self, context: Any) -> str: ...
    def get_agent_user_id_from_webhook(self, webhook_id: str) -> str | None: ...
    def _2fa_disabled_legacy(self, entity_id: str) -> bool | None: ...
    def should_2fa(self, state: State) -> bool: ...
    async def async_report_state(self, message: Any, agent_user_id: str, event_id: str | None = None) -> None: ...
    async def _async_request_sync_devices(self, agent_user_id: str) -> HTTPStatus | int: ...
    async def async_connect_agent_user(self, agent_user_id: str) -> None: ...
    async def async_disconnect_agent_user(self, agent_user_id: str) -> None: ...
    @callback
    def async_get_agent_users(self) -> tuple: ...
    async def _async_prefs_updated(self, prefs: CloudPreferences) -> None: ...
    @callback
    def _async_exposed_entities_updated(self) -> None: ...
    @callback
    def _handle_entity_registry_updated(self, event: Event[er.EventEntityRegistryUpdatedData]) -> None: ...
    @callback
    def _handle_device_registry_updated(self, event: Event[dr.EventDeviceRegistryUpdatedData]) -> None: ...
