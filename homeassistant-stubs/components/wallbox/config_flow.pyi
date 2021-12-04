from . import InvalidAuth as InvalidAuth, WallboxCoordinator as WallboxCoordinator
from .const import CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries, core as core
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

COMPONENT_DOMAIN = DOMAIN
STEP_USER_DATA_SCHEMA: Any

async def validate_input(hass: core.HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class ConfigFlow(config_entries.ConfigFlow):
    _reauth_entry: Any
    def __init__(self) -> None: ...
    async def async_step_reauth(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
    async def async_step_user(self, user_input: Union[dict[str, Any], None] = ...) -> FlowResult: ...
