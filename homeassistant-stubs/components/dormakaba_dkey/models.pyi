from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from py_dormakaba_dkey import DKEYLock as DKEYLock

class DormakabaDkeyData:
    lock: DKEYLock
    coordinator: DataUpdateCoordinator[None]
    def __init__(self, lock, coordinator) -> None: ...
