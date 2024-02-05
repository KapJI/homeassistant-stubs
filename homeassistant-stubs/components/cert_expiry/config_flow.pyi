from .const import DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN
from .errors import ConnectionRefused as ConnectionRefused, ConnectionTimeout as ConnectionTimeout, ResolveFailed as ResolveFailed, ValidationFailure as ValidationFailure
from .helper import get_cert_expiry_timestamp as get_cert_expiry_timestamp
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.data_entry_flow import FlowResult as FlowResult
from typing import Any

_LOGGER: Incomplete

class CertexpiryConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    _errors: Incomplete
    def __init__(self) -> None: ...
    async def _test_connection(self, user_input: Mapping[str, Any]) -> bool: ...
    async def async_step_user(self, user_input: Mapping[str, Any] | None = None) -> FlowResult: ...
    async def async_step_import(self, user_input: Mapping[str, Any] | None = None) -> FlowResult: ...
