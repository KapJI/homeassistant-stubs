from .const import CONF_SYSTEM_ZONE as CONF_SYSTEM_ZONE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_FILENAME as CONF_FILENAME
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete

async def _enumerate_sz(tty: str) -> list[tuple[int, int]]: ...

class BryantConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reconfigure_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
