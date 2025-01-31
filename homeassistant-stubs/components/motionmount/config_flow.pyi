import asyncio
from .const import DOMAIN as DOMAIN, EMPTY_MAC as EMPTY_MAC
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, DEFAULT_DISCOVERY_UNIQUE_ID as DEFAULT_DISCOVERY_UNIQUE_ID, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PIN as CONF_PIN, CONF_PORT as CONF_PORT, CONF_UUID as CONF_UUID
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from typing import Any

_LOGGER: Incomplete

class MotionMountFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    connection_data: dict[str, Any]
    backoff_task: asyncio.Task | None
    backoff_time: int
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, user_input: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_auth(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_backoff(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def _create_or_update_entry(self) -> ConfigFlowResult: ...
    async def _validate_input_connect(self, data: dict) -> dict[str, Any]: ...
    async def _validate_input_pin(self, data: dict) -> bool | int: ...
    def _show_setup_form(self, errors: dict[str, str] | None = None) -> ConfigFlowResult: ...
    async def _backoff(self, time: int) -> None: ...
