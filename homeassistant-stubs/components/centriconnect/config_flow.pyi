import probatio
from .const import CENTRICONNECT_DEVICE_ID as CENTRICONNECT_DEVICE_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any, override

_LOGGER: Incomplete
STEP_RECONFIGURE_DATA_SCHEMA: Incomplete
STEP_REAUTHENTICATE_DATA_SCHEMA: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]: ...

class CentriConnectConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _device_id: str | None
    async def _handle_flow(self, step_id: str, data_schema: probatio.Schema, user_input: dict[str, Any] | None, update_user_input: Callable[[dict[str, Any]], dict[str, Any]], on_success: Callable[[dict[str, Any], dict[str, Any]], ConfigFlowResult]) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
