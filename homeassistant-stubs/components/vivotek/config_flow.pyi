from . import VivotekConfigEntry as VivotekConfigEntry, build_cam_client as build_cam_client
from .camera import DEFAULT_FRAMERATE as DEFAULT_FRAMERATE, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_STREAM_SOURCE as DEFAULT_STREAM_SOURCE
from .const import CONF_FRAMERATE as CONF_FRAMERATE, CONF_SECURITY_LEVEL as CONF_SECURITY_LEVEL, CONF_STREAM_PATH as CONF_STREAM_PATH, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow
from homeassistant.const import CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, HTTP_BASIC_AUTHENTICATION as HTTP_BASIC_AUTHENTICATION, HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION, UnitOfFrequency as UnitOfFrequency
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

_LOGGER: Incomplete
DESCRIPTION_PLACEHOLDERS: Incomplete
CONF_SCHEMA: Incomplete
OPTIONS_SCHEMA: Incomplete

class OptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class VivotekConfigFlow(ConfigFlow, domain=DOMAIN):
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: VivotekConfigEntry) -> OptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...
