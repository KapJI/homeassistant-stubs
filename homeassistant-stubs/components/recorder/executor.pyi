from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.util.executor import InterruptibleThreadPoolExecutor as InterruptibleThreadPoolExecutor
from typing import Any

def _worker_with_shutdown_hook(shutdown_hook: Callable[[], None], *args: Any, **kwargs: Any) -> None: ...

class DBInterruptibleThreadPoolExecutor(InterruptibleThreadPoolExecutor):
    _shutdown_hook: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def _adjust_thread_count(self) -> None: ...
