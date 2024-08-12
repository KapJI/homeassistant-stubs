from .const import DEFAULT_NAME as DEFAULT_NAME, DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN
from .errors import CannotConnect as CannotConnect
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from madvr.madvr import Madvr
from typing import Any

_LOGGER: Incomplete
STEP_USER_DATA_SCHEMA: Incomplete
RETRY_INTERVAL: int

class MadVRConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def _test_connection(self, host: str, port: int) -> str: ...
    async def _close_test_connection(self, madvr_client: Madvr) -> None: ...
