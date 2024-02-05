from . import async_connect_androidtv as async_connect_androidtv, get_androidtv_mac as get_androidtv_mac
from .const import CONF_ADBKEY as CONF_ADBKEY, CONF_ADB_SERVER_IP as CONF_ADB_SERVER_IP, CONF_ADB_SERVER_PORT as CONF_ADB_SERVER_PORT, CONF_APPS as CONF_APPS, CONF_EXCLUDE_UNNAMED_APPS as CONF_EXCLUDE_UNNAMED_APPS, CONF_GET_SOURCES as CONF_GET_SOURCES, CONF_SCREENCAP as CONF_SCREENCAP, CONF_STATE_DETECTION_RULES as CONF_STATE_DETECTION_RULES, CONF_TURN_OFF_COMMAND as CONF_TURN_OFF_COMMAND, CONF_TURN_ON_COMMAND as CONF_TURN_ON_COMMAND, DEFAULT_ADB_SERVER_PORT as DEFAULT_ADB_SERVER_PORT, DEFAULT_DEVICE_CLASS as DEFAULT_DEVICE_CLASS, DEFAULT_EXCLUDE_UNNAMED_APPS as DEFAULT_EXCLUDE_UNNAMED_APPS, DEFAULT_GET_SOURCES as DEFAULT_GET_SOURCES, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_SCREENCAP as DEFAULT_SCREENCAP, DEVICE_CLASSES as DEVICE_CLASSES, DOMAIN as DOMAIN, PROP_ETHMAC as PROP_ETHMAC, PROP_WIFIMAC as PROP_WIFIMAC
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, OptionsFlowWithConfigEntry as OptionsFlowWithConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.selector import ObjectSelector as ObjectSelector, SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

APPS_NEW_ID: str
CONF_APP_DELETE: str
CONF_APP_ID: str
CONF_APP_NAME: str
RULES_NEW_ID: str
CONF_RULE_DELETE: str
CONF_RULE_ID: str
CONF_RULE_VALUES: str
RESULT_CONN_ERROR: str
RESULT_UNKNOWN: str
_LOGGER: Incomplete

def _is_file(value: str) -> bool: ...

class AndroidTVFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    def _show_setup_form(self, user_input: dict[str, Any] | None = None, error: str | None = None) -> FlowResult: ...
    async def _async_check_connection(self, user_input: dict[str, Any]) -> tuple[str | None, str | None]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlowHandler: ...

class OptionsFlowHandler(OptionsFlowWithConfigEntry):
    _apps: Incomplete
    _state_det_rules: Incomplete
    _conf_app_id: Incomplete
    _conf_rule_id: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    def _save_config(self, data: dict[str, Any]) -> FlowResult: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    def _async_init_form(self) -> FlowResult: ...
    async def async_step_apps(self, user_input: dict[str, Any] | None = None, app_id: str | None = None) -> FlowResult: ...
    def _async_apps_form(self, app_id: str) -> FlowResult: ...
    async def async_step_rules(self, user_input: dict[str, Any] | None = None, rule_id: str | None = None) -> FlowResult: ...
    def _async_rules_form(self, rule_id: str, default_id: str = '', errors: dict[str, str] | None = None) -> FlowResult: ...

def _validate_state_det_rules(state_det_rules: Any) -> list[Any] | None: ...
