from .const import DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN
from .errors import ConnectionRefused as ConnectionRefused, ConnectionReset as ConnectionReset, ConnectionTimeout as ConnectionTimeout, ResolveFailed as ResolveFailed, ValidationFailure as ValidationFailure
from .helper import get_cert_expiry_timestamp as get_cert_expiry_timestamp
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from typing import Any

class CertexpiryConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _errors: dict[str, str]
    def __init__(self) -> None: ...
    async def _test_connection(self, user_input: Mapping[str, Any]) -> bool: ...
    async def async_step_user(self, user_input: Mapping[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: Mapping[str, Any] | None = None) -> ConfigFlowResult: ...
