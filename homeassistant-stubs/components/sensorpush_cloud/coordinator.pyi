from .const import LOGGER as LOGGER, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_EMAIL as CONF_EMAIL, CONF_PASSWORD as CONF_PASSWORD
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from sensorpush_ha import SensorPushCloudData

type SensorPushCloudConfigEntry = ConfigEntry[SensorPushCloudCoordinator]
class SensorPushCloudCoordinator(DataUpdateCoordinator[dict[str, SensorPushCloudData]]):
    helper: Incomplete
    def __init__(self, hass: HomeAssistant, entry: SensorPushCloudConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, SensorPushCloudData]: ...
