from homeassistant.components.cover import SUPPORT_CLOSE as SUPPORT_CLOSE, SUPPORT_OPEN as SUPPORT_OPEN
from homeassistant.const import STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from typing import Any, Final

NOTIFICATION_ID: Final[str]
NOTIFICATION_TITLE: Final[str]
STATES_MAP: Final[dict[str, str]]
SUPPORTED_FEATURES: Final[Any]
