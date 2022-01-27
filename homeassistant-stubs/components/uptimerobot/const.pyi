from datetime import timedelta
from homeassistant.const import Platform as Platform
from logging import Logger
from typing import Any, Final

LOGGER: Logger
COORDINATOR_UPDATE_INTERVAL: timedelta
DOMAIN: Final[str]
PLATFORMS: Final[Any]
ATTRIBUTION: Final[str]
ATTR_TARGET: Final[str]
API_ATTR_OK: Final[str]
