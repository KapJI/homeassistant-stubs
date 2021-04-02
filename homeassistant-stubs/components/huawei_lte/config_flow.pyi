from .const import CONNECTION_TIMEOUT as CONNECTION_TIMEOUT, DEFAULT_DEVICE_NAME as DEFAULT_DEVICE_NAME, DEFAULT_NOTIFY_SERVICE_NAME as DEFAULT_NOTIFY_SERVICE_NAME, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries
from homeassistant.components import ssdp as ssdp
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_RECIPIENT as CONF_RECIPIENT, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from typing import Any

_LOGGER: Any

class ConfigFlowHandler(config_entries.ConfigFlow):
    VERSION: int = ...
    CONNECTION_CLASS: Any = ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> OptionsFlowHandler: ...
    async def _async_show_user_form(self, user_input: Union[dict[str, Any], None]=..., errors: Union[dict[str, str], None]=...) -> dict[str, Any]: ...
    async def async_step_import(self, user_input: Union[dict[str, Any], None]=...) -> dict[str, Any]: ...
    def _already_configured(self, user_input: dict[str, Any]) -> bool: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None]=...) -> dict[str, Any]: ...
    async def async_step_ssdp(self, discovery_info: dict[str, Any]) -> dict[str, Any]: ...

class OptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Any = ...
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: Union[dict[str, Any], None]=...) -> dict[str, Any]: ...
