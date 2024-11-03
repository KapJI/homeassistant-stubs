import asyncio
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

_LOGGER: Incomplete
_TERMINATE_TIMEOUT: int
_SETUP_TIMEOUT: int
_SUCCESSFUL_BOOT_MESSAGE: str
_LOCALHOST_IP: str
_GO2RTC_CONFIG_FORMAT: str

def _create_temp_file(api_ip: str) -> str: ...

class Server:
    _hass: Incomplete
    _binary: Incomplete
    _process: Incomplete
    _startup_complete: Incomplete
    _api_ip: Incomplete
    def __init__(self, hass: HomeAssistant, binary: str, *, enable_ui: bool = False) -> None: ...
    async def start(self) -> None: ...
    async def _log_output(self, process: asyncio.subprocess.Process) -> None: ...
    async def stop(self) -> None: ...
