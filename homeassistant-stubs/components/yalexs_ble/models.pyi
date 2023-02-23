from yalexs_ble import PushLock as PushLock

class YaleXSBLEData:
    title: str
    lock: PushLock
    def __init__(self, title, lock) -> None: ...
