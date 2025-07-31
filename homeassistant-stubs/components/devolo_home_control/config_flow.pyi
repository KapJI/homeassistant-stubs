from . import configure_mydevolo as configure_mydevolo
from .const import DOMAIN as DOMAIN, SUPPORTED_MODEL_TYPES as SUPPORTED_MODEL_TYPES
from .exceptions import CredentialsInvalid as CredentialsInvalid, UuidChanged as UuidChanged
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers.service_info.zeroconf import ZeroconfServiceInfo as ZeroconfServiceInfo
from typing import Any

DATA_SCHEMA: Incomplete

class DevoloHomeControlFlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_zeroconf_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _connect_mydevolo(self, user_input: dict[str, Any]) -> ConfigFlowResult: ...
