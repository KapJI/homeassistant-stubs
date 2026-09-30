from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from lyngdorf import LyngdorfReceiver as LyngdorfReceiver

@dataclass
class LyngdorfRuntimeData:
    receiver: LyngdorfReceiver
    device_info: DeviceInfo
    zone_b_device_info: DeviceInfo | None
type LyngdorfConfigEntry = ConfigEntry[LyngdorfRuntimeData]
