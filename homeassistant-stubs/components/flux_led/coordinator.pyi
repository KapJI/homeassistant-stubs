from .const import FLUX_LED_EXCEPTIONS as FLUX_LED_EXCEPTIONS
from flux_led.aio import AIOWifiLedBulb as AIOWifiLedBulb
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, Final

_LOGGER: Any
REQUEST_REFRESH_DELAY: Final[float]

class FluxLedUpdateCoordinator(DataUpdateCoordinator):
    device: Any
    title: Any
    entry: Any
    def __init__(self, hass: HomeAssistant, device: AIOWifiLedBulb, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...
