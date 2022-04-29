import voluptuous as vol
from . import DOMAIN as DOMAIN
from .binary_sensor import CONF_ALL as CONF_ALL
from .const import CONF_HIDE_MEMBERS as CONF_HIDE_MEMBERS
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant.const import CONF_ENTITIES as CONF_ENTITIES
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er, selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep, SchemaFlowMenuStep as SchemaFlowMenuStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler, entity_selector_without_own_entities as entity_selector_without_own_entities
from typing import Any

def basic_group_options_schema(domain: str, handler: Union[SchemaConfigFlowHandler, SchemaOptionsFlowHandler], options: dict[str, Any]) -> vol.Schema: ...
def basic_group_config_schema(domain: str) -> vol.Schema: ...
def binary_sensor_options_schema(handler: Union[SchemaConfigFlowHandler, SchemaOptionsFlowHandler], options: dict[str, Any]) -> vol.Schema: ...

BINARY_SENSOR_CONFIG_SCHEMA: Incomplete

def light_switch_options_schema(domain: str, handler: Union[SchemaConfigFlowHandler, SchemaOptionsFlowHandler], options: dict[str, Any]) -> vol.Schema: ...

GROUP_TYPES: Incomplete

def choose_options_step(options: dict[str, Any]) -> str: ...
def set_group_type(group_type: str) -> Callable[[dict[str, Any]], dict[str, Any]]: ...

CONFIG_FLOW: dict[str, Union[SchemaFlowFormStep, SchemaFlowMenuStep]]
OPTIONS_FLOW: dict[str, Union[SchemaFlowFormStep, SchemaFlowMenuStep]]

class GroupConfigFlowHandler(SchemaConfigFlowHandler):
    config_flow: Incomplete
    options_flow: Incomplete
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
    def async_config_flow_finished(self, options: Mapping[str, Any]) -> None: ...
    @staticmethod
    def async_options_flow_finished(hass: HomeAssistant, options: Mapping[str, Any]) -> None: ...

def _async_hide_members(hass: HomeAssistant, members: list[str], hidden_by: Union[er.RegistryEntryHider, None]) -> None: ...
