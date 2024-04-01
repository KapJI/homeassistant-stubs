from .const import CONF_STATION as CONF_STATION, DOMAIN as DOMAIN
from .coordinator import InvalidAuth as InvalidAuth, WallboxCoordinator as WallboxCoordinator
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

COMPONENT_DOMAIN = DOMAIN
STEP_USER_DATA_SCHEMA: Incomplete

async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, str]: ...

class WallboxConfigFlow(ConfigFlow, domain=COMPONENT_DOMAIN):
    _reauth_entry: Incomplete
    def __init__(self) -> None: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
