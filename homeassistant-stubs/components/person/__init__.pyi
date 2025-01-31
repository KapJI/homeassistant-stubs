from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.auth import EVENT_USER_REMOVED as EVENT_USER_REMOVED
from homeassistant.components import persistent_notification as persistent_notification, websocket_api as websocket_api
from homeassistant.components.device_tracker import ATTR_SOURCE_TYPE as ATTR_SOURCE_TYPE, SourceType as SourceType
from homeassistant.const import ATTR_EDITABLE as ATTR_EDITABLE, ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, ATTR_ID as ATTR_ID, ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_NAME as ATTR_NAME, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, SERVICE_RELOAD as SERVICE_RELOAD, STATE_HOME as STATE_HOME, STATE_NOT_HOME as STATE_NOT_HOME, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers import collection as collection, entity_registry as er, service as service
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, Self

_LOGGER: Incomplete
ATTR_SOURCE: str
ATTR_USER_ID: str
ATTR_DEVICE_TRACKERS: str
CONF_DEVICE_TRACKERS: str
CONF_USER_ID: str
CONF_PICTURE: str
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
IGNORE_STATES: Incomplete
PERSON_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

@bind_hass
async def async_create_person(hass: HomeAssistant, name: str, *, user_id: str | None = None, device_trackers: list[str] | None = None) -> None: ...
@bind_hass
async def async_add_user_device_tracker(hass: HomeAssistant, user_id: str, device_tracker_entity_id: str) -> None: ...
@callback
def persons_with_entity(hass: HomeAssistant, entity_id: str) -> list[str]: ...
@callback
def entities_in_person(hass: HomeAssistant, entity_id: str) -> list[str]: ...

CREATE_FIELDS: VolDictType
UPDATE_FIELDS: VolDictType

class PersonStore(Store):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...

class PersonStorageCollection(collection.DictStorageCollection):
    CREATE_SCHEMA: Incomplete
    UPDATE_SCHEMA: Incomplete
    yaml_collection: Incomplete
    def __init__(self, store: Store, id_manager: collection.IDManager, yaml_collection: collection.YamlCollection) -> None: ...
    async def _async_load_data(self) -> collection.SerializedStorageCollection | None: ...
    async def async_load(self) -> None: ...
    @callback
    def _entity_registry_filter(self, event_data: er.EventEntityRegistryUpdatedData) -> bool: ...
    async def _entity_registry_updated(self, event: Event[er.EventEntityRegistryUpdatedData]) -> None: ...
    async def _process_create_data(self, data: dict) -> dict: ...
    @callback
    def _get_suggested_id(self, info: dict[str, str]) -> str: ...
    async def _update_data(self, item: dict, update_data: dict) -> dict: ...
    async def _validate_user_id(self, user_id: str) -> None: ...

class PersonStorageCollectionWebsocket(collection.DictStorageCollectionWebsocket):
    def ws_list_item(self, hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...

async def filter_yaml_data(hass: HomeAssistant, persons: list[dict]) -> list[dict]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class Person(collection.CollectionEntity, RestoreEntity):
    _entity_component_unrecorded_attributes: Incomplete
    _attr_should_poll: bool
    editable: bool
    _config: Incomplete
    _latitude: float | None
    _longitude: float | None
    _gps_accuracy: float | None
    _source: str | None
    _unsub_track_device: Callable[[], None] | None
    _attr_state: str | None
    device_trackers: list[str]
    _attr_unique_id: Incomplete
    def __init__(self, config: dict[str, Any]) -> None: ...
    _attr_name: Incomplete
    _attr_entity_picture: Incomplete
    def _set_attrs_from_config(self) -> None: ...
    @classmethod
    def from_storage(cls, config: ConfigType) -> Self: ...
    @classmethod
    def from_yaml(cls, config: ConfigType) -> Self: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_update_config(self, config: ConfigType) -> None: ...
    @callback
    def _async_update_config(self, config: ConfigType) -> None: ...
    @callback
    def _async_handle_tracker_update(self, event: Event[EventStateChangedData]) -> None: ...
    @callback
    def _update_state(self) -> None: ...
    @callback
    def _parse_source_state(self, state: State) -> None: ...
    _attr_extra_state_attributes: Incomplete
    @callback
    def _update_extra_state_attributes(self) -> None: ...

def _get_latest(prev: State | None, curr: State) -> State: ...
