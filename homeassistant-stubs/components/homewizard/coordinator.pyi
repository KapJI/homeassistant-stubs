import aiohwenergy
from .const import DOMAIN as DOMAIN, DeviceResponseEntry as DeviceResponseEntry, UPDATE_INTERVAL as UPDATE_INTERVAL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

_LOGGER: Any

class HWEnergyDeviceUpdateCoordinator(DataUpdateCoordinator[DeviceResponseEntry]):
    api: aiohwenergy.HomeWizardEnergy
    def __init__(self, hass: HomeAssistant, host: str) -> None: ...
    async def _async_update_data(self) -> DeviceResponseEntry: ...
    async def initialize_api(self) -> aiohwenergy: ...
