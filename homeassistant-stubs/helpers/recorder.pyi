import asyncio
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

DOMAIN: str

class RecorderData:
    recorder_platforms: dict[str, Any]
    db_connected: asyncio.Future
    def __init__(self, recorder_platforms, db_connected) -> None: ...

def async_migration_in_progress(hass: HomeAssistant) -> bool: ...
def async_initialize_recorder(hass: HomeAssistant) -> None: ...
async def async_wait_recorder(hass: HomeAssistant) -> bool: ...
