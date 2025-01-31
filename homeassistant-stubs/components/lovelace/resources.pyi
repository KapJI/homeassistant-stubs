from .const import CONF_RESOURCE_TYPE_WS as CONF_RESOURCE_TYPE_WS, DOMAIN as DOMAIN, RESOURCE_CREATE_FIELDS as RESOURCE_CREATE_FIELDS, RESOURCE_SCHEMA as RESOURCE_SCHEMA, RESOURCE_UPDATE_FIELDS as RESOURCE_UPDATE_FIELDS
from .dashboard import LovelaceConfig as LovelaceConfig
from .websocket import websocket_lovelace_resources_impl as websocket_lovelace_resources_impl
from _typeshed import Incomplete
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import CONF_ID as CONF_ID, CONF_RESOURCES as CONF_RESOURCES, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import collection as collection, storage as storage
from typing import Any

RESOURCE_STORAGE_KEY: Incomplete
RESOURCES_STORAGE_VERSION: int
_LOGGER: Incomplete

class ResourceYAMLCollection:
    loaded: bool
    data: Incomplete
    def __init__(self, data: list[dict[str, Any]]) -> None: ...
    async def async_get_info(self) -> dict[str, int]: ...
    @callback
    def async_items(self) -> list[dict]: ...

class ResourceStorageCollection(collection.DictStorageCollection):
    loaded: bool
    CREATE_SCHEMA: Incomplete
    UPDATE_SCHEMA: Incomplete
    ll_config: Incomplete
    def __init__(self, hass: HomeAssistant, ll_config: LovelaceConfig) -> None: ...
    async def async_get_info(self) -> dict[str, int]: ...
    async def _async_load_data(self) -> collection.SerializedStorageCollection | None: ...
    async def _process_create_data(self, data: dict) -> dict: ...
    @callback
    def _get_suggested_id(self, info: dict) -> str: ...
    async def _update_data(self, item: dict, update_data: dict) -> dict: ...

class ResourceStorageCollectionWebsocket(collection.DictStorageCollectionWebsocket):
    @callback
    def async_setup(self, hass: HomeAssistant) -> None: ...
    @staticmethod
    @websocket_api.async_response
    async def ws_list_item(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
