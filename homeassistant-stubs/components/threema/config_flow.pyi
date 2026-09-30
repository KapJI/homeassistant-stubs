from .client import ThreemaAPIClient as ThreemaAPIClient, ThreemaAuthError as ThreemaAuthError, ThreemaConnectionError as ThreemaConnectionError, derive_public_key as derive_public_key, generate_key_pair as generate_key_pair
from .const import CONF_API_SECRET as CONF_API_SECRET, CONF_GATEWAY_ID as CONF_GATEWAY_ID, CONF_PRIVATE_KEY as CONF_PRIVATE_KEY, DOMAIN as DOMAIN, SUBENTRY_TYPE_RECIPIENT as SUBENTRY_TYPE_RECIPIENT
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, ConfigSubentryFlow as ConfigSubentryFlow, SubentryFlowResult as SubentryFlowResult
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_RECIPIENT as CONF_RECIPIENT
from homeassistant.core import callback as callback
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from typing import Any, override

_LOGGER: Incomplete
_KEY_HEX_LENGTH: int
_KEY_PREFIXES: Incomplete
_CONF_PUBLIC_KEY: str
_GATEWAY_ID_REGEX: Incomplete

def _strip_key_prefix(value: str, expected_prefix: str) -> str | None: ...
def _is_valid_key_hex(value: str) -> bool: ...

class ThreemaConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    @classmethod
    @callback
    @override
    def async_get_supported_subentry_types(cls, config_entry: ConfigEntry) -> dict[str, type[ConfigSubentryFlow]]: ...
    _gateway_id: str | None
    _api_secret: str | None
    _private_key: str | None
    _public_key: str | None
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_setup_new(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_credentials(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

_RECIPIENT_ID_REGEX: Incomplete

class RecipientSubentryFlowHandler(ConfigSubentryFlow):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> SubentryFlowResult: ...
