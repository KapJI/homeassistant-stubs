from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .helpers import get_device_id as get_device_id, get_unique_id as get_unique_id, get_valueless_base_unique_id as get_valueless_base_unique_id
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.value import Value as ZwaveValue

EVENT_VALUE_UPDATED: str
EVENT_VALUE_REMOVED: str
EVENT_DEAD: str
EVENT_ALIVE: str

class ZWaveBaseEntity(Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    config_entry: Incomplete
    driver: Incomplete
    info: Incomplete
    watched_value_ids: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_assumed_state: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    def on_value_update(self) -> None: ...
    async def async_poll_value(self, refresh_all_values: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def generate_name(self, include_value_name: bool = ..., alternate_value_name: Union[str, None] = ..., additional_info: Union[list[str], None] = ..., name_prefix: Union[str, None] = ...) -> str: ...
    @property
    def available(self) -> bool: ...
    def _node_status_alive_or_dead(self, event_data: dict) -> None: ...
    def _value_changed(self, event_data: dict) -> None: ...
    def _value_removed(self, event_data: dict) -> None: ...
    def get_zwave_value(self, value_property: Union[str, int], command_class: Union[int, None] = ..., endpoint: Union[int, None] = ..., value_property_key: Union[int, str, None] = ..., add_to_watched_value_ids: bool = ..., check_all_endpoints: bool = ...) -> Union[ZwaveValue, None]: ...
