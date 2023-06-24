from .const import CONF_IMEI as CONF_IMEI, CONF_OTP as CONF_OTP, CONF_PHONE_NUMBER as CONF_PHONE_NUMBER, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _phone_number: Incomplete
    _description_placeholders: Incomplete
    _otp: Incomplete
    _imei: Incomplete
    _token: Incomplete
    _api: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    def _show_setup_form(self, user_input: dict[str, str] | None = ..., errors: dict[str, str] | None = ..., step_id: str = ...) -> FlowResult: ...
    async def _validate_phone_number(self, user_input: dict[str, str]) -> FlowResult: ...
    async def _validate_one_time_password(self, user_input: dict[str, str]) -> FlowResult: ...
    async def async_step_one_time_password(self, user_input: dict[str, Any] | None = ..., errors: dict[str, str] | None = ...) -> FlowResult: ...
    async def _show_otp_form(self, errors: dict[str, str] | None = ...) -> FlowResult: ...
