from .const import DOMAIN as DOMAIN, DeviceResponseEntry as DeviceResponseEntry, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homewizard_energy import HomeWizardEnergy

_LOGGER: Incomplete
MAX_UPDATE_INTERVAL: Incomplete

class HWEnergyDeviceUpdateCoordinator(DataUpdateCoordinator[DeviceResponseEntry]):
    api: HomeWizardEnergy
    api_disabled: bool
    entry_id: Incomplete
    def __init__(self, hass: HomeAssistant, entry_id: str, host: str) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def _async_update_data(self) -> DeviceResponseEntry: ...
