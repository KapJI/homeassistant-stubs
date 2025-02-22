import dataclasses
from .const import DATA_EXPOSED_ENTITIES as DATA_EXPOSED_ENTITIES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import CLOUD_NEVER_EXPOSED_ENTITIES as CLOUD_NEVER_EXPOSED_ENTITIES
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.entity import get_device_class as get_device_class
from homeassistant.helpers.storage import Store as Store
from homeassistant.util.read_only_dict import ReadOnlyDict as ReadOnlyDict
from typing import Any, TypedDict

KNOWN_ASSISTANTS: Incomplete
STORAGE_KEY: Incomplete
STORAGE_VERSION: int
SAVE_DELAY: int
DEFAULT_EXPOSED_DOMAINS: Incomplete
DEFAULT_EXPOSED_BINARY_SENSOR_DEVICE_CLASSES: Incomplete
DEFAULT_EXPOSED_SENSOR_DEVICE_CLASSES: Incomplete
DEFAULT_EXPOSED_ASSISTANT: Incomplete

@dataclasses.dataclass(frozen=True)
class AssistantPreferences:
    expose_new: bool
    def to_json(self) -> dict[str, Any]: ...

@dataclasses.dataclass(frozen=True)
class ExposedEntity:
    assistants: dict[str, dict[str, Any]]
    def to_json(self) -> dict[str, Any]: ...

class SerializedExposedEntities(TypedDict):
    assistants: dict[str, dict[str, Any]]
    exposed_entities: dict[str, dict[str, Any]]

class ExposedEntities:
    _assistants: dict[str, AssistantPreferences]
    entities: dict[str, ExposedEntity]
    _hass: Incomplete
    _listeners: dict[str, list[Callable[[], None]]]
    _store: Store[SerializedExposedEntities]
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_initialize(self) -> None: ...
    @callback
    def async_listen_entity_updates(self, assistant: str, listener: Callable[[], None]) -> CALLBACK_TYPE: ...
    @callback
    def async_set_assistant_option(self, assistant: str, entity_id: str, key: str, value: Any) -> None: ...
    def _async_set_legacy_assistant_option(self, assistant: str, entity_id: str, key: str, value: Any) -> None: ...
    @callback
    def async_get_expose_new_entities(self, assistant: str) -> bool: ...
    @callback
    def async_set_expose_new_entities(self, assistant: str, expose_new: bool) -> None: ...
    @callback
    def async_get_assistant_settings(self, assistant: str) -> dict[str, Mapping[str, Any]]: ...
    @callback
    def async_get_entity_settings(self, entity_id: str) -> dict[str, Mapping[str, Any]]: ...
    @callback
    def async_should_expose(self, assistant: str, entity_id: str) -> bool: ...
    def _async_should_expose_legacy_entity(self, assistant: str, entity_id: str) -> bool: ...
    def _is_default_exposed(self, entity_id: str, registry_entry: er.RegistryEntry | None) -> bool: ...
    def _update_exposed_entity(self, assistant: str, entity_id: str, key: str, value: Any) -> ExposedEntity: ...
    def _new_exposed_entity(self, assistant: str, key: str, value: Any) -> ExposedEntity: ...
    async def _async_load_data(self) -> SerializedExposedEntities | None: ...
    @callback
    def _async_schedule_save(self) -> None: ...
    @callback
    def _data_to_save(self) -> SerializedExposedEntities: ...

@callback
@websocket_api.require_admin
def ws_expose_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def ws_list_exposed_entities(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def ws_expose_new_entities_get(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
@websocket_api.require_admin
def ws_expose_new_entities_set(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
@callback
def async_listen_entity_updates(hass: HomeAssistant, assistant: str, listener: Callable[[], None]) -> CALLBACK_TYPE: ...
@callback
def async_get_assistant_settings(hass: HomeAssistant, assistant: str) -> dict[str, Mapping[str, Any]]: ...
@callback
def async_get_entity_settings(hass: HomeAssistant, entity_id: str) -> dict[str, Mapping[str, Any]]: ...
@callback
def async_expose_entity(hass: HomeAssistant, assistant: str, entity_id: str, should_expose: bool) -> None: ...
@callback
def async_should_expose(hass: HomeAssistant, assistant: str, entity_id: str) -> bool: ...
@callback
def async_set_assistant_option(hass: HomeAssistant, assistant: str, entity_id: str, option: str, value: Any) -> None: ...
