from .const import DOMAIN as DOMAIN, DeviceResponseEntry as DeviceResponseEntry, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homewizard_energy import HomeWizardEnergy

_LOGGER: Incomplete

class HWEnergyDeviceUpdateCoordinator(DataUpdateCoordinator[DeviceResponseEntry]):
    api: HomeWizardEnergy
    api_disabled: bool
    entry: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, host: str) -> None: ...
    async def _async_update_data(self) -> DeviceResponseEntry: ...
