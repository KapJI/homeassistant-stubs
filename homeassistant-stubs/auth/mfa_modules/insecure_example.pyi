import voluptuous as vol
from . import MULTI_FACTOR_AUTH_MODULES as MULTI_FACTOR_AUTH_MODULES, MULTI_FACTOR_AUTH_MODULE_SCHEMA as MULTI_FACTOR_AUTH_MODULE_SCHEMA, MultiFactorAuthModule as MultiFactorAuthModule, SetupFlow as SetupFlow
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

CONFIG_SCHEMA: Any

class InsecureExampleModule(MultiFactorAuthModule):
    DEFAULT_TITLE: str
    _data: Any
    def __init__(self, hass: HomeAssistant, config: dict[str, Any]) -> None: ...
    @property
    def input_schema(self) -> vol.Schema: ...
    @property
    def setup_schema(self) -> vol.Schema: ...
    async def async_setup_flow(self, user_id: str) -> SetupFlow: ...
    async def async_setup_user(self, user_id: str, setup_data: Any) -> Any: ...
    async def async_depose_user(self, user_id: str) -> None: ...
    async def async_is_user_setup(self, user_id: str) -> bool: ...
    async def async_validate(self, user_id: str, user_input: dict[str, Any]) -> bool: ...
