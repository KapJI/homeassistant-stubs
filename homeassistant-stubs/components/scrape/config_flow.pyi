from . import COMBINED_SCHEMA as COMBINED_SCHEMA
from .const import CONF_ADVANCED as CONF_ADVANCED, CONF_AUTH as CONF_AUTH, CONF_ENCODING as CONF_ENCODING, CONF_INDEX as CONF_INDEX, CONF_SELECT as CONF_SELECT, DEFAULT_ENCODING as DEFAULT_ENCODING, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import data_entry_flow as data_entry_flow
from homeassistant.components.rest import create_rest_data_from_config as create_rest_data_from_config
from homeassistant.components.rest.data import DEFAULT_TIMEOUT as DEFAULT_TIMEOUT
from homeassistant.components.rest.schema import DEFAULT_METHOD as DEFAULT_METHOD, METHODS as METHODS
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, FlowType as FlowType, OptionsFlow as OptionsFlow, SOURCE_USER as SOURCE_USER, SubentryFlowContext as SubentryFlowContext, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_HEADERS as CONF_HEADERS, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PAYLOAD as CONF_PAYLOAD, CONF_RESOURCE as CONF_RESOURCE, CONF_TIMEOUT as CONF_TIMEOUT, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_USERNAME as CONF_USERNAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, CONF_VERIFY_SSL as CONF_VERIFY_SSL, HTTP_BASIC_AUTHENTICATION as HTTP_BASIC_AUTHENTICATION, HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.selector import BooleanSelector as BooleanSelector, NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, NumberSelectorMode as NumberSelectorMode, ObjectSelector as ObjectSelector, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TemplateSelector as TemplateSelector, TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY
from typing import Any

_LOGGER: Incomplete
RESOURCE_SETUP: Incomplete
SENSOR_SETTINGS: Incomplete
SENSOR_SETUP: Incomplete

async def validate_rest_setup(hass: HomeAssistant, user_input: dict[str, Any]) -> dict[str, Any]: ...

class ScrapeConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> ScrapeOptionFlow: ...
    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_on_create_entry(self, result: ConfigFlowResult) -> ConfigFlowResult: ...

class ScrapeOptionFlow(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class ScrapeSubentryFlowHandler(ConfigSubentryFlow):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
