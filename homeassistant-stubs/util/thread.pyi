import threading
from typing import Any

def _async_raise(tid: int, exctype: Any) -> None: ...

class ThreadWithException(threading.Thread):
    def raise_exc(self, exctype: Any) -> None: ...
