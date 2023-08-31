from yalexs_ble import PushLock as PushLock

class YaleXSBLEData:
    title: str
    lock: PushLock
    always_connected: bool
    def __init__(self, title, lock, always_connected) -> None: ...
