from .const import DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .helpers import get_device_id as get_device_id, get_unique_id as get_unique_id
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from typing import Any
from zwave_js_server.client import Client as ZwaveClient
from zwave_js_server.model.value import Value as ZwaveValue

LOGGER: Any
EVENT_VALUE_UPDATED: str
EVENT_DEAD: str
EVENT_ALIVE: str

class ZWaveBaseEntity(Entity):
    config_entry: Any
    client: Any
    info: Any
    watched_value_ids: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_entity_registry_enabled_default: Any
    _attr_assumed_state: Any
    _attr_device_info: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    def on_value_update(self) -> None: ...
    async def async_poll_value(self, refresh_all_values: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def generate_name(self, include_value_name: bool = ..., alternate_value_name: Union[str, None] = ..., additional_info: Union[list[str], None] = ..., name_suffix: Union[str, None] = ...) -> str: ...
    @property
    def available(self) -> bool: ...
    def _node_status_alive_or_dead(self, event_data: dict) -> None: ...
    def _value_changed(self, event_data: dict) -> None: ...
    def get_zwave_value(self, value_property: Union[str, int], command_class: Union[int, None] = ..., endpoint: Union[int, None] = ..., value_property_key: Union[int, None] = ..., add_to_watched_value_ids: bool = ..., check_all_endpoints: bool = ...) -> Union[ZwaveValue, None]: ...
    @property
    def should_poll(self) -> bool: ...
