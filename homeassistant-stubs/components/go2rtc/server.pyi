import asyncio
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

_LOGGER: Incomplete
_TERMINATE_TIMEOUT: int
_SETUP_TIMEOUT: int
_SUCCESSFUL_BOOT_MESSAGE: str
_GO2RTC_CONFIG: str

def _create_temp_file() -> str: ...

class Server:
    _hass: Incomplete
    _binary: Incomplete
    _process: Incomplete
    _startup_complete: Incomplete
    def __init__(self, hass: HomeAssistant, binary: str) -> None: ...
    async def start(self) -> None: ...
    async def _log_output(self, process: asyncio.subprocess.Process) -> None: ...
    async def stop(self) -> None: ...
