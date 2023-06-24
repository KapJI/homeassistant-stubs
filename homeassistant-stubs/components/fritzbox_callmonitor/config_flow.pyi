import voluptuous as vol
from .base import FritzBoxPhonebook as FritzBoxPhonebook
from .const import CONF_PHONEBOOK as CONF_PHONEBOOK, CONF_PREFIXES as CONF_PREFIXES, DEFAULT_HOST as DEFAULT_HOST, DEFAULT_PHONEBOOK as DEFAULT_PHONEBOOK, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_USERNAME as DEFAULT_USERNAME, DOMAIN as DOMAIN, FRITZ_ATTR_NAME as FRITZ_ATTR_NAME, FRITZ_ATTR_SERIAL_NUMBER as FRITZ_ATTR_SERIAL_NUMBER, SERIAL_NUMBER as SERIAL_NUMBER
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import callback as callback
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

DATA_SCHEMA_USER: Incomplete

class ConnectResult(StrEnum):
    INVALID_AUTH: str
    INSUFFICIENT_PERMISSIONS: str
    MALFORMED_PREFIXES: str
    NO_DEVIES_FOUND: str
    SUCCESS: str

class FritzBoxCallMonitorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _host: str
    _port: int
    _username: str
    _password: str
    _phonebook_name: str
    _phonebook_id: int
    _phonebook_ids: list[int]
    _fritzbox_phonebook: FritzBoxPhonebook
    _serial_number: str
    _phonebook_names: Incomplete
    def __init__(self) -> None: ...
    def _get_config_entry(self) -> FlowResult: ...
    def _try_connect(self) -> ConnectResult: ...
    async def _get_name_of_phonebook(self, phonebook_id: int) -> str: ...
    async def _get_list_of_phonebook_names(self) -> list[str]: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> FritzBoxCallMonitorOptionsFlowHandler: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_phonebook(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...

class FritzBoxCallMonitorOptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    @classmethod
    def _are_prefixes_valid(cls, prefixes: str | None) -> bool: ...
    @classmethod
    def _get_list_of_prefixes(cls, prefixes: str | None) -> list[str] | None: ...
    def _get_option_schema_prefixes(self) -> vol.Schema: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
