import asyncio
from homeassistant import bootstrap as bootstrap
from homeassistant.core import callback as callback
from homeassistant.helpers.frame import warn_use as warn_use
from homeassistant.util.executor import InterruptibleThreadPoolExecutor as InterruptibleThreadPoolExecutor
from homeassistant.util.thread import deadlock_safe_shutdown as deadlock_safe_shutdown
from typing import Any

MAX_EXECUTOR_WORKERS: int

class RuntimeConfig:
    config_dir: str
    skip_pip: bool
    safe_mode: bool
    verbose: bool
    log_rotate_days: Union[int, None]
    log_file: Union[str, None]
    log_no_color: bool
    debug: bool
    open_ui: bool

class HassEventLoopPolicy(asyncio.DefaultEventLoopPolicy):
    debug: Any
    def __init__(self, debug: bool) -> None: ...
    @property
    def loop_name(self) -> str: ...
    def new_event_loop(self) -> asyncio.AbstractEventLoop: ...

def _async_loop_exception_handler(_: Any, context: dict[str, Any]) -> None: ...
async def setup_and_run_hass(runtime_config: RuntimeConfig) -> int: ...
def run(runtime_config: RuntimeConfig) -> int: ...
