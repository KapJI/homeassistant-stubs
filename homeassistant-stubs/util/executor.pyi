from concurrent.futures import ThreadPoolExecutor
from homeassistant.util.thread import async_raise as async_raise
from threading import Thread
from typing import Any

_LOGGER: Any
MAX_LOG_ATTEMPTS: int
_JOIN_ATTEMPTS: int
EXECUTOR_SHUTDOWN_TIMEOUT: int

def _log_thread_running_at_shutdown(name: str, ident: int) -> None: ...
def join_or_interrupt_threads(threads: set[Thread], timeout: float, log: bool) -> set[Thread]: ...

class InterruptibleThreadPoolExecutor(ThreadPoolExecutor):
    _shutdown: bool
    def shutdown(self, *args, **kwargs) -> None: ...
    def join_threads_or_timeout(self) -> None: ...
