from bleak.backends.device import BLEDevice as BLEDevice
from pysnooz.device import SnoozDevice as SnoozDevice

class SnoozConfigurationData:
    ble_device: BLEDevice
    device: SnoozDevice
    title: str
    def __init__(self, ble_device, device, title) -> None: ...
