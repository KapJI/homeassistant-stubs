from homeassistant.const import HTTP_HEADER_X_REQUESTED_WITH as HTTP_HEADER_X_REQUESTED_WITH
from homeassistant.core import callback as callback
from typing import Any

ALLOWED_CORS_HEADERS: Any
VALID_CORS_TYPES: Any

def setup_cors(app: Any, origins: Any): ...
