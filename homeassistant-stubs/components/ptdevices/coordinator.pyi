from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioptdevices.interface import Interface as Interface, PTDevicesResponseData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, REQUEST_REFRESH_DEFAULT_IMMEDIATE as REQUEST_REFRESH_DEFAULT_IMMEDIATE, UpdateFailed as UpdateFailed
from typing import Final

_LOGGER: Incomplete
REFRESH_COOLDOWN: Final[int]
UPDATE_INTERVAL: Incomplete
type PTDevicesConfigEntry = ConfigEntry[PTDevicesCoordinator]

class PTDevicesCoordinator(DataUpdateCoordinator[PTDevicesResponseData]):
    config_entry: PTDevicesConfigEntry
    interface: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: PTDevicesConfigEntry, ptdevices_interface: Interface) -> None: ...
    async def _async_update_data(self) -> PTDevicesResponseData: ...
