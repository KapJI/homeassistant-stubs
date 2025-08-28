import voluptuous as vol
from .binary_sensor import above_greater_than_below as above_greater_than_below, no_overlapping as no_overlapping
from .const import CONF_OBSERVATIONS as CONF_OBSERVATIONS, CONF_PRIOR as CONF_PRIOR, CONF_PROBABILITY_THRESHOLD as CONF_PROBABILITY_THRESHOLD, CONF_P_GIVEN_F as CONF_P_GIVEN_F, CONF_P_GIVEN_T as CONF_P_GIVEN_T, CONF_TEMPLATE as CONF_TEMPLATE, CONF_TO_STATE as CONF_TO_STATE, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PROBABILITY_THRESHOLD as DEFAULT_PROBABILITY_THRESHOLD, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from enum import StrEnum
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlowResult as ConfigFlowResult, ConfigSubentry as ConfigSubentry, ConfigSubentryData as ConfigSubentryData, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_ABOVE as CONF_ABOVE, CONF_BELOW as CONF_BELOW, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM, CONF_STATE as CONF_STATE, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import callback as callback
from homeassistant.helpers import selector as selector, translation as translation
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaConfigFlowHandler as SchemaConfigFlowHandler, SchemaFlowError as SchemaFlowError, SchemaFlowFormStep as SchemaFlowFormStep, SchemaFlowMenuStep as SchemaFlowMenuStep
from typing import Any

_LOGGER: Incomplete
USER: str
OBSERVATION_SELECTOR: str
ALLOWED_STATE_DOMAINS: Incomplete
ALLOWED_NUMERIC_DOMAINS: Incomplete

class ObservationTypes(StrEnum):
    STATE = CONF_STATE
    NUMERIC_STATE = 'numeric_state'
    TEMPLATE = CONF_TEMPLATE

class OptionsFlowSteps(StrEnum):
    INIT = 'init'
    ADD_OBSERVATION = OBSERVATION_SELECTOR

OPTIONS_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
OBSERVATION_BOILERPLATE: Incomplete
STATE_SUBSCHEMA: Incomplete
NUMERIC_STATE_SUBSCHEMA: Incomplete
TEMPLATE_SUBSCHEMA: Incomplete

def _convert_percentages_to_fractions(data: dict[str, str | float | int]) -> dict[str, str | float]: ...
def _convert_fractions_to_percentages(data: dict[str, str | float]) -> dict[str, str | float]: ...
def _select_observation_schema(obs_type: ObservationTypes) -> vol.Schema: ...
async def _get_base_suggested_values(handler: SchemaCommonFlowHandler) -> dict[str, Any]: ...
def _get_observation_values_for_editing(subentry: ConfigSubentry) -> dict[str, Any]: ...
async def _validate_user(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
def _validate_observation_subentry(obs_type: ObservationTypes, user_input: dict[str, Any], other_subentries: list[dict[str, Any]] | None = None) -> dict[str, Any]: ...
async def _validate_subentry_from_config_entry(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def _get_description_placeholders(handler: SchemaCommonFlowHandler) -> dict[str, str]: ...
async def _get_observation_menu_options(handler: SchemaCommonFlowHandler) -> list[str]: ...

CONFIG_FLOW: dict[str, SchemaFlowMenuStep | SchemaFlowFormStep]
OPTIONS_FLOW: dict[str, SchemaFlowMenuStep | SchemaFlowFormStep]

class BayesianConfigFlowHandler(SchemaConfigFlowHandler, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    config_flow = CONFIG_FLOW
    options_flow = OPTIONS_FLOW
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    def async_config_entry_title(self, options: Mapping[str, str]) -> str: ...
    @callback
    def async_create_entry(self, data: Mapping[str, Any], **kwargs: Any) -> ConfigFlowResult: ...

class ObservationSubentryFlowHandler(ConfigSubentryFlow):
    async def step_common(self, user_input: dict[str, Any] | None, obs_type: ObservationTypes, reconfiguring: bool = False) -> SubentryFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_state(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_numeric_state(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_template(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
