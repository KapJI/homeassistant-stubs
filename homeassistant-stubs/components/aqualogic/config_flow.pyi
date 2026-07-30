from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from typing import Any, override

STEP_USER_DATA_SCHEMA: Incomplete
_PROBE_TIMEOUT: Incomplete

class CannotConnect(Exception): ...
class InvalidDevice(Exception): ...

def _verify_device(host: str, port: int) -> None: ...

class AquaLogicConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    @override
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...
