import asyncio
from . import bootstrap as bootstrap
from .core import callback as callback
from .helpers.frame import warn_use as warn_use
from .util.executor import InterruptibleThreadPoolExecutor as InterruptibleThreadPoolExecutor
from .util.thread import deadlock_safe_shutdown as deadlock_safe_shutdown
from _typeshed import Incomplete
from typing import Any

MAX_EXECUTOR_WORKERS: int
TASK_CANCELATION_TIMEOUT: int
_LOGGER: Incomplete

class RuntimeConfig:
    config_dir: str
    skip_pip: bool
    skip_pip_packages: list[str]
    recovery_mode: bool
    verbose: bool
    log_rotate_days: int | None
    log_file: str | None
    log_no_color: bool
    debug: bool
    open_ui: bool
    safe_mode: bool
    def __init__(self, config_dir, skip_pip, skip_pip_packages, recovery_mode, verbose, log_rotate_days, log_file, log_no_color, debug, open_ui, safe_mode) -> None: ...

def can_use_pidfd() -> bool: ...

class HassEventLoopPolicy(asyncio.DefaultEventLoopPolicy):
    debug: Incomplete
    _watcher: Incomplete
    def __init__(self, debug: bool) -> None: ...
    def _init_watcher(self) -> None: ...
    @property
    def loop_name(self) -> str: ...
    def new_event_loop(self) -> asyncio.AbstractEventLoop: ...

def _async_loop_exception_handler(_: Any, context: dict[str, Any]) -> None: ...
async def setup_and_run_hass(runtime_config: RuntimeConfig) -> int: ...
def _enable_posix_spawn() -> None: ...
def run(runtime_config: RuntimeConfig) -> int: ...
def _cancel_all_tasks_with_timeout(loop: asyncio.AbstractEventLoop, timeout: int) -> None: ...
