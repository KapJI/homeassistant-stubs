import asyncio
from .const import HA_MANAGED_API_PORT as HA_MANAGED_API_PORT, HA_MANAGED_URL as HA_MANAGED_URL
from .util import get_go2rtc_unix_socket_path as get_go2rtc_unix_socket_path
from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from collections import deque
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

_LOGGER: Incomplete
_TERMINATE_TIMEOUT: int
_SETUP_TIMEOUT: int
_SUCCESSFUL_BOOT_MESSAGE: str
_LOG_BUFFER_SIZE: int
_RESPAWN_COOLDOWN: int
_GO2RTC_CONFIG_FORMAT: str
_APP_MODULES: Incomplete
_API_ALLOW_PATHS: Incomplete
_UI_APP_MODULES: Incomplete
_UI_API_ALLOW_PATHS: Incomplete
_LOG_LEVEL_MAP: Incomplete

class Go2RTCServerStartError(HomeAssistantError):
    _message: str

class Go2RTCWatchdogError(HomeAssistantError): ...

def _format_list_for_yaml(items: tuple[str, ...]) -> str: ...
def _create_temp_file(enable_ui: bool, username: str, password: str, working_dir: str) -> str: ...

class Server:
    _hass: Incomplete
    _binary: Incomplete
    _session: Incomplete
    _enable_ui: Incomplete
    _username: Incomplete
    _password: Incomplete
    _working_dir: Incomplete
    _log_buffer: deque[str]
    _process: asyncio.subprocess.Process | None
    _startup_complete: Incomplete
    _watchdog_task: asyncio.Task | None
    _watchdog_tasks: list[asyncio.Task]
    def __init__(self, hass: HomeAssistant, binary: str, session: ClientSession, *, enable_ui: bool = False, username: str, password: str, working_dir: str) -> None: ...
    async def start(self) -> None: ...
    async def _start(self) -> None: ...
    async def _log_output(self, process: asyncio.subprocess.Process) -> None: ...
    def _log_server_output(self, loglevel: int) -> None: ...
    async def _watchdog(self) -> None: ...
    async def _monitor_process(self) -> None: ...
    async def _monitor_api(self) -> None: ...
    async def _stop_watchdog(self) -> None: ...
    async def stop(self) -> None: ...
    async def _stop(self) -> None: ...
