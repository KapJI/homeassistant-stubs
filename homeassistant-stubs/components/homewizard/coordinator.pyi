from .const import DOMAIN as DOMAIN, ISSUE_BATTERY_MODE_CLOUD_DISABLED as ISSUE_BATTERY_MODE_CLOUD_DISABLED, LOGGER as LOGGER, UPDATE_INTERVAL as UPDATE_INTERVAL, battery_mode_cloud_issue_id as battery_mode_cloud_issue_id
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homewizard_energy import HomeWizardEnergy as HomeWizardEnergy
from homewizard_energy.models import CombinedModels as DeviceResponseEntry

type HomeWizardConfigEntry = ConfigEntry[HWEnergyDeviceUpdateCoordinator]
class HWEnergyDeviceUpdateCoordinator(DataUpdateCoordinator[DeviceResponseEntry]):
    api: HomeWizardEnergy
    api_disabled: bool
    config_entry: HomeWizardConfigEntry
    def __init__(self, hass: HomeAssistant, config_entry: HomeWizardConfigEntry, api: HomeWizardEnergy) -> None: ...
    def _update_battery_mode_cloud_repair_issue(self, data: DeviceResponseEntry) -> None: ...
    data: Incomplete
    async def _async_update_data(self) -> DeviceResponseEntry: ...
