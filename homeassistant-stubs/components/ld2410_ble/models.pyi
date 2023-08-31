from .coordinator import LD2410BLECoordinator as LD2410BLECoordinator
from ld2410_ble import LD2410BLE as LD2410BLE

class LD2410BLEData:
    title: str
    device: LD2410BLE
    coordinator: LD2410BLECoordinator
    def __init__(self, title, device, coordinator) -> None: ...
