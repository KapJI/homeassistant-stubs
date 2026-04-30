from bleak.backends.device import BLEDevice as BLEDevice
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from pysnooz.device import SnoozDevice as SnoozDevice

type SnoozConfigEntry = ConfigEntry[SnoozConfigurationData]
@dataclass
class SnoozConfigurationData:
    ble_device: BLEDevice
    device: SnoozDevice
    title: str
