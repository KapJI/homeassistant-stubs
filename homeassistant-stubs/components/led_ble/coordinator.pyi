from .const import UPDATE_SECONDS as UPDATE_SECONDS
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from led_ble import LEDBLE as LEDBLE

type LEDBLEConfigEntry = ConfigEntry[LEDBLEData]
@dataclass
class LEDBLEData:
    title: str
    device: LEDBLE
    coordinator: LEDBLECoordinator

_LOGGER: Incomplete

class LEDBLECoordinator(DataUpdateCoordinator[None]):
    config_entry: LEDBLEConfigEntry
    led_ble: Incomplete
    def __init__(self, hass: HomeAssistant, entry: LEDBLEConfigEntry, led_ble: LEDBLE) -> None: ...
    async def _async_update_data(self) -> None: ...
