import voluptuous as vol
from . import DEFAULT_FADE_RATE as DEFAULT_FADE_RATE, calculate_unique_id as calculate_unique_id
from .const import CONF_ADDR as CONF_ADDR, CONF_BUTTONS as CONF_BUTTONS, CONF_CONTROLLER_ID as CONF_CONTROLLER_ID, CONF_DIMMERS as CONF_DIMMERS, CONF_INDEX as CONF_INDEX, CONF_KEYPADS as CONF_KEYPADS, CONF_LED as CONF_LED, CONF_NUMBER as CONF_NUMBER, CONF_RATE as CONF_RATE, CONF_RELEASE_DELAY as CONF_RELEASE_DELAY, DEFAULT_BUTTON_NAME as DEFAULT_BUTTON_NAME, DEFAULT_KEYPAD_NAME as DEFAULT_KEYPAD_NAME, DEFAULT_LIGHT_NAME as DEFAULT_LIGHT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import async_get_hass as async_get_hass, callback as callback
from homeassistant.data_entry_flow import AbortFlow as AbortFlow
from homeassistant.helpers import selector as selector
from homeassistant.helpers.schema_config_entry_flow import SchemaCommonFlowHandler as SchemaCommonFlowHandler, SchemaFlowError as SchemaFlowError, SchemaFlowFormStep as SchemaFlowFormStep, SchemaFlowMenuStep as SchemaFlowMenuStep, SchemaOptionsFlowHandler as SchemaOptionsFlowHandler
from homeassistant.helpers.selector import TextSelector as TextSelector
from homeassistant.helpers.typing import VolDictType as VolDictType
from homeassistant.util import slugify as slugify
from typing import Any

_LOGGER: Incomplete
CONTROLLER_EDIT: Incomplete
LIGHT_EDIT: VolDictType
BUTTON_EDIT: VolDictType
validate_addr: Incomplete

def _validate_credentials(user_input: dict[str, Any]) -> None: ...
async def validate_add_controller(handler: ConfigFlow | SchemaOptionsFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def _try_connection(user_input: dict[str, Any]) -> None: ...
def _validate_address(handler: SchemaCommonFlowHandler, addr: str) -> None: ...
def _validate_button_number(handler: SchemaCommonFlowHandler, number: int) -> None: ...
async def validate_add_button(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def validate_add_keypad(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def validate_add_light(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def get_select_button_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def get_select_keypad_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def get_select_light_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def validate_select_button(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def validate_select_keypad_light(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def get_edit_button_suggested_values(handler: SchemaCommonFlowHandler) -> dict[str, Any]: ...
async def get_edit_light_suggested_values(handler: SchemaCommonFlowHandler) -> dict[str, Any]: ...
async def validate_button_edit(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def validate_light_edit(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def get_remove_button_schema(handler: SchemaCommonFlowHandler) -> vol.Schema: ...
async def get_remove_keypad_light_schema(handler: SchemaCommonFlowHandler, *, key: str) -> vol.Schema: ...
async def validate_remove_button(handler: SchemaCommonFlowHandler, user_input: dict[str, Any]) -> dict[str, Any]: ...
async def validate_remove_keypad_light(handler: SchemaCommonFlowHandler, user_input: dict[str, Any], *, key: str) -> dict[str, Any]: ...

DATA_SCHEMA_ADD_CONTROLLER: Incomplete
DATA_SCHEMA_EDIT_CONTROLLER: Incomplete
DATA_SCHEMA_ADD_LIGHT: Incomplete
DATA_SCHEMA_ADD_KEYPAD: Incomplete
DATA_SCHEMA_ADD_BUTTON: Incomplete
DATA_SCHEMA_EDIT_BUTTON: Incomplete
DATA_SCHEMA_EDIT_LIGHT: Incomplete
OPTIONS_FLOW: Incomplete

class HomeworksConfigFlowHandler(ConfigFlow, domain=DOMAIN):
    async def _validate_edit_controller(self, user_input: dict[str, Any]) -> dict[str, Any]: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> SchemaOptionsFlowHandler: ...
