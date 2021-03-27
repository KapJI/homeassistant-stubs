import threading
from typing import Any

class ThreadWithException(threading.Thread):
    def raise_exc(self, exctype: Any) -> None: ...
