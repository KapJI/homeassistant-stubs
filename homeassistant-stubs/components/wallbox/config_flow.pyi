from .const import CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from .coordinator import InvalidAuth as InvalidAuth, WallboxCoordinator as WallboxCoordinator
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries, core as core
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

COMPONENT_DOMAIN = DOMAIN
STEP_USER_DATA_SCHEMA: Incomplete

async def validate_input(hass: core.HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class ConfigFlow(config_entries.ConfigFlow, domain=COMPONENT_DOMAIN):
    _reauth_entry: Incomplete
    def __init__(self) -> None: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
