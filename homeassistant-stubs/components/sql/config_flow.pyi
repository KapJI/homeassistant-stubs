import voluptuous as vol
from .const import CONF_ADVANCED_OPTIONS as CONF_ADVANCED_OPTIONS, CONF_COLUMN_NAME as CONF_COLUMN_NAME, CONF_QUERY as CONF_QUERY, DOMAIN as DOMAIN
from .util import EmptyQueryError as EmptyQueryError, InvalidSqlQuery as InvalidSqlQuery, MultipleQueryError as MultipleQueryError, NotSelectQueryError as NotSelectQueryError, UnknownQueryTypeError as UnknownQueryTypeError, check_and_render_sql_query as check_and_render_sql_query, resolve_db_url as resolve_db_url
from _typeshed import Incomplete
from homeassistant.components.recorder import CONF_DB_URL as CONF_DB_URL, get_instance as get_instance
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, SensorDeviceClass as SensorDeviceClass, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithReload as OptionsFlowWithReload
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import async_get_hass as async_get_hass, callback as callback
from homeassistant.data_entry_flow import section as section
from homeassistant.exceptions import TemplateError as TemplateError
from homeassistant.helpers import selector as selector
from sqlalchemy.engine import Engine as Engine, Result as Result
from sqlalchemy.orm import Session as Session
from typing import Any

_LOGGER: Incomplete
OPTIONS_SCHEMA: vol.Schema
CONFIG_SCHEMA: vol.Schema

def validate_sql_select(value: str) -> str: ...
def validate_db_connection(db_url: str) -> bool: ...
def validate_query(db_url: str, query: str, column: str) -> bool: ...

class SQLConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    data: dict[str, Any]
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> SQLOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_options(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class SQLOptionsFlowHandler(OptionsFlowWithReload):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
