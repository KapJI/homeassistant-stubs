from .const import CONF_INSTALLATION_ID as CONF_INSTALLATION_ID, CONF_MODEL as CONF_MODEL, CONF_SERIAL as CONF_SERIAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_USERNAME as CONF_USERNAME
from homeassistant.helpers import selector as selector
from homeassistant.helpers.redact import async_redact_data as async_redact_data
from homeassistant.helpers.service_info.ssdp import SsdpServiceInfo as SsdpServiceInfo
from typing import Any

DEFAULT_HOST: str
DEFAULT_PORT: int
_LOGGER: Incomplete
TO_REDACT: Incomplete
ENTRY_TITLE_FORMAT: str
STEP_USER_DATA_SCHEMA: Incomplete
STEP_SSDP_AUTH_DATA_SCHEMA: Incomplete
STEP_REAUTH_DATA_SCHEMA: Incomplete

async def validate_input(data: dict[str, Any]) -> str: ...

class VictronGXConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    hostname: str | None
    serial: str | None
    installation_id: str | None
    friendly_name: str | None
    model_name: str | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_ssdp(self, discovery_info: SsdpServiceInfo) -> ConfigFlowResult: ...
    async def async_step_ssdp_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_ssdp_auth(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, _: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
