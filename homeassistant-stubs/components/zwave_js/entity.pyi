from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .helpers import get_device_id as get_device_id, get_unique_id as get_unique_id, get_valueless_base_unique_id as get_valueless_base_unique_id
from _typeshed import Incomplete
from collections.abc import Sequence
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED
from typing import Any
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.value import SetValueResult as SetValueResult, Value as ZwaveValue

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
    _attr_entity_registry_enabled_default: bool
    _attr_entity_category: Incomplete
    _attr_assumed_state: bool
    _attr_device_info: Incomplete
    def __init__(self, config_entry: ConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    def on_value_update(self) -> None: ...
    async def _async_poll_value(self, value_or_id: str | ZwaveValue) -> None: ...
    async def async_poll_value(self, refresh_all_values: bool) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def generate_name(self, include_value_name: bool = ..., alternate_value_name: str | None = ..., additional_info: Sequence[str | None] | None = ..., name_prefix: str | None = ...) -> str: ...
    @property
    def available(self) -> bool: ...
    def _node_status_alive_or_dead(self, event_data: dict) -> None: ...
    def _value_changed(self, event_data: dict) -> None: ...
    def _value_removed(self, event_data: dict) -> None: ...
    def get_zwave_value(self, value_property: str | int, command_class: int | None = ..., endpoint: int | None = ..., value_property_key: int | str | None = ..., add_to_watched_value_ids: bool = ..., check_all_endpoints: bool = ...) -> ZwaveValue | None: ...
    async def _async_set_value(self, value: ZwaveValue, new_value: Any, options: dict | None = ..., wait_for_result: bool | None = ...) -> SetValueResult | None: ...
