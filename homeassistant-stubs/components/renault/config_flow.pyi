from .const import DOMAIN as DOMAIN, RenaultConfigurationKeys as RenaultConfigurationKeys
from .renault_hub import RenaultHub as RenaultHub
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE
from typing import Any, override

_LOGGER: Incomplete
USER_SCHEMA: Incomplete
REAUTH_SCHEMA: Incomplete

class RenaultFlowHandler(ConfigFlow, domain=DOMAIN):
    renault_hub: RenaultHub
    renault_config: dict[str, Any]
    def __init__(self) -> None: ...
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_kamereon(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: Mapping[str, Any]) -> ConfigFlowResult: ...
