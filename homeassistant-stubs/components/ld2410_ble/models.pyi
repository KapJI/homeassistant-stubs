from .coordinator import LD2410BLECoordinator as LD2410BLECoordinator
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from ld2410_ble import LD2410BLE as LD2410BLE

type LD2410BLEConfigEntry = ConfigEntry[LD2410BLEData]
@dataclass
class LD2410BLEData:
    title: str
    device: LD2410BLE
    coordinator: LD2410BLECoordinator
