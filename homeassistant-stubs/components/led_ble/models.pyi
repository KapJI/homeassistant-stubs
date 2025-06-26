from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from led_ble import LEDBLE as LEDBLE

type LEDBLEConfigEntry = ConfigEntry[LEDBLEData]
@dataclass
class LEDBLEData:
    title: str
    device: LEDBLE
    coordinator: DataUpdateCoordinator[None]
