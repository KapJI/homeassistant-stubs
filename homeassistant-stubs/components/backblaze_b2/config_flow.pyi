from .const import BACKBLAZE_REALM as BACKBLAZE_REALM, CONF_APPLICATION_KEY as CONF_APPLICATION_KEY, CONF_BUCKET as CONF_BUCKET, CONF_KEY_ID as CONF_KEY_ID, CONF_PREFIX as CONF_PREFIX, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any

_LOGGER: Incomplete
REQUIRED_CAPABILITIES: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

class BackblazeConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    reauth_entry: ConfigEntry[Any] | None
    def _abort_if_duplicate_credentials(self, user_input: dict[str, Any]) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _async_validate_backblaze_connection(self, user_input: dict[str, Any]) -> tuple[dict[str, str], dict[str, str]]: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
