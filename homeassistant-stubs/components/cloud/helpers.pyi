import logging
from collections import deque
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import override

class FixedSizeQueueLogHandler(logging.Handler):
    MAX_RECORDS: int
    _records: deque[logging.LogRecord]
    def __init__(self) -> None: ...
    @override
    def emit(self, record: logging.LogRecord) -> None: ...
    async def get_logs(self, hass: HomeAssistant) -> list[str]: ...
