from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send, dispatcher_connect as dispatcher_connect
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, create_issue as create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
SIGNAL_DISCOVER_PLATFORM: str
SIGNAL_MESSAGE_REQUEST: str
SIGNAL_MESSAGE_UPDATE: str
SIGNAL_CDR_UPDATE: str
SIGNAL_CDR_REQUEST: str
CONFIG_SCHEMA: Incomplete

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class AsteriskData:
    hass: Incomplete
    config: Incomplete
    messages: Incomplete
    cdr: Incomplete
    client: Incomplete
    def __init__(self, hass: HomeAssistant, host: str, port: int, password: str, config: dict[str, Any]) -> None: ...
    def _discover_platform(self, component: str) -> None: ...
    def handle_data(self, command: int, msg: list[dict[str, Any]] | dict[str, Any]) -> None: ...
    def _request_messages(self) -> None: ...
    def _request_cdr(self) -> None: ...
