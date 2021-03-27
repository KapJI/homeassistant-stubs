from .connection import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from typing import Any

WebSocketCommandHandler: Any
DOMAIN: str
URL: str
PENDING_MSG_PEAK: int
PENDING_MSG_PEAK_TIME: int
MAX_PENDING_MSG: int
ERR_ID_REUSE: str
ERR_INVALID_FORMAT: str
ERR_NOT_FOUND: str
ERR_NOT_SUPPORTED: str
ERR_HOME_ASSISTANT_ERROR: str
ERR_UNKNOWN_COMMAND: str
ERR_UNKNOWN_ERROR: str
ERR_UNAUTHORIZED: str
ERR_TIMEOUT: str
ERR_TEMPLATE_ERROR: str
TYPE_RESULT: str
CANCELLATION_ERRORS: Any
SIGNAL_WEBSOCKET_CONNECTED: str
SIGNAL_WEBSOCKET_DISCONNECTED: str
DATA_CONNECTIONS: Any
JSON_DUMP: Any
