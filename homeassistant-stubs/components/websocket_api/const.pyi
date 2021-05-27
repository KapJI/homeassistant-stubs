from .connection import ActiveConnection as ActiveConnection
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from typing import Any, Final

WebSocketCommandHandler: Any
AsyncWebSocketCommandHandler: Any
DOMAIN: Final[str]
URL: Final[str]
PENDING_MSG_PEAK: Final[int]
PENDING_MSG_PEAK_TIME: Final[int]
MAX_PENDING_MSG: Final[int]
ERR_ID_REUSE: Final[str]
ERR_INVALID_FORMAT: Final[str]
ERR_NOT_FOUND: Final[str]
ERR_NOT_SUPPORTED: Final[str]
ERR_HOME_ASSISTANT_ERROR: Final[str]
ERR_UNKNOWN_COMMAND: Final[str]
ERR_UNKNOWN_ERROR: Final[str]
ERR_UNAUTHORIZED: Final[str]
ERR_TIMEOUT: Final[str]
ERR_TEMPLATE_ERROR: Final[str]
TYPE_RESULT: Final[str]
CANCELLATION_ERRORS: Final[Any]
SIGNAL_WEBSOCKET_CONNECTED: Final[str]
SIGNAL_WEBSOCKET_DISCONNECTED: Final[str]
DATA_CONNECTIONS: Final[Any]
JSON_DUMP: Final[Any]
