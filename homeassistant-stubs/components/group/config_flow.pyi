import voluptuous as vol
from . import DOMAIN as DOMAIN
from .binary_sensor import CONF_ALL as CONF_ALL
from .const import CONF_HIDE_MEMBERS as CONF_HIDE_MEMBERS, CONF_IGNORE_NON_NUMERIC as CONF_IGNORE_NON_NUMERIC
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Mapping
from homeassistant.const import CONF_ENTITIES as CONF_ENTITIES, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er, selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowFormStep as SchemaFlowFormStep, SchemaFlowMenuStep as SchemaFlowMenuStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler, entity_selector_without_own_entities as entity_selector_without_own_entities
from typing import Any

_STATISTIC_MEASURES: Incomplete

async def basic_group_options_schema(domain: str | list[str], handler: SchemaCommonFlowHandler) -> vol.Schema: ...
def basic_group_config_schema(domain: str | list[str]) -> vol.Schema: ...
async def binary_sensor_options_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...

BINARY_SENSOR_CONFIG_SCHEMA: Incomplete
SENSOR_CONFIG_EXTENDS: Incomplete
SENSOR_OPTIONS: Incomplete

async def sensor_options_schema(domain: str, handler: SchemaCommonFlowHandler) -> vol.Schema: ...

SENSOR_CONFIG_SCHEMA: Incomplete

async def light_switch_options_schema(domain: str, handler: SchemaCommonFlowHandler) -> vol.Schema: ...

GROUP_TYPES: Incomplete

async def choose_options_step(options: dict[str, Any]) -> str: ...
def set_group_type(group_type: str) -> Callable[[SchemaCommonFlowHandler, dict[str, Any]], Coroutine[Any, Any, dict[str, Any]]]: ...

CONFIG_FLOW: Incomplete
OPTIONS_FLOW: Incomplete

class GroupConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    def async_config_entry_title(self, options: Mapping[str, Any]) -> str: ...
    def async_config_flow_finished(self, options: Mapping[str, Any]) -> None: ...
    @staticmethod
    def async_options_flow_finished(hass: HomeAssistant, options: Mapping[str, Any]) -> None: ...

def _async_hide_members(hass: HomeAssistant, members: list[str], hidden_by: er.RegistryEntryHider | None) -> None: ...
