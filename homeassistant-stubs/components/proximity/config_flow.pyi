import voluptuous as vol
from .const import CONF_IGNORED_ZONES as CONF_IGNORED_ZONES, CONF_TOLERANCE as CONF_TOLERANCE, CONF_TRACKED_ENTITIES as CONF_TRACKED_ENTITIES, DEFAULT_PROXIMITY_ZONE as DEFAULT_PROXIMITY_ZONE, DEFAULT_TOLERANCE as DEFAULT_TOLERANCE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_ZONE as CONF_ZONE
from homeassistant.core import State as State, callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.selector import EntitySelector as EntitySelector, EntitySelectorConfig as EntitySelectorConfig, NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig
from homeassistant.util import slugify as slugify
from typing import Any

RESULT_SUCCESS: str

def _base_schema(user_input: dict[str, Any]) -> vol.Schema: ...

class ProximityConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    def _user_form_schema(self, user_input: dict[str, Any] | None = None) -> vol.Schema: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_import(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...

class ProximityOptionsFlow(OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    def _user_form_schema(self, user_input: dict[str, Any]) -> vol.Schema: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
