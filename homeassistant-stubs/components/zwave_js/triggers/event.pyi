from ..const import ATTR_EVENT as ATTR_EVENT, ATTR_EVENT_DATA as ATTR_EVENT_DATA, ATTR_EVENT_SOURCE as ATTR_EVENT_SOURCE, ATTR_NODE_ID as ATTR_NODE_ID, ATTR_PARTIAL_DICT_MATCH as ATTR_PARTIAL_DICT_MATCH, DOMAIN as DOMAIN
from ..helpers import async_get_nodes_from_targets as async_get_nodes_from_targets, get_device_id as get_device_id, get_home_and_node_id_from_device_entry as get_home_and_node_id_from_device_entry
from .trigger_helpers import async_bypass_dynamic_config_validation as async_bypass_dynamic_config_validation
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import ATTR_CONFIG_ENTRY_ID as ATTR_CONFIG_ENTRY_ID, ATTR_DEVICE_ID as ATTR_DEVICE_ID, ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.automation import move_top_level_schema_fields_to_options as move_top_level_schema_fields_to_options
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.trigger import Trigger as Trigger, TriggerActionRunner as TriggerActionRunner, TriggerConfig as TriggerConfig
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from zwave_js_server.model.driver import Driver as Driver

RELATIVE_PLATFORM_TYPE: Incomplete
PLATFORM_TYPE: Incomplete

def validate_non_node_event_source(obj: dict) -> dict: ...
def validate_event_name(obj: dict) -> dict: ...
def validate_event_data(obj: dict) -> dict: ...

_OPTIONS_SCHEMA_DICT: Incomplete
_CONFIG_SCHEMA: Incomplete

class EventTrigger(Trigger):
    _options: dict[str, Any]
    _event_source: str
    _event_name: str
    _event_data_filter: dict
    _unsubs: list[Callable]
    _action_runner: TriggerActionRunner
    @classmethod
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    async def async_attach_runner(self, run_action: TriggerActionRunner) -> CALLBACK_TYPE: ...
    @callback
    def _async_on_event(self, event_data: dict, device: dr.DeviceEntry | None = None) -> None: ...
    @callback
    def _async_remove(self) -> None: ...
    @callback
    def _create_zwave_listeners(self) -> None: ...
