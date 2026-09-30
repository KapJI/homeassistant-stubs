from .const import DOMAIN as DOMAIN
from .util import get_ssl_context as get_ssl_context
from _typeshed import Incomplete
from aioindiallsky import ExposureData as ExposureData, MediaData as MediaData, SensorData
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete
type IndiAllSkyConfigEntry = ConfigEntry[IndiAllSkyDataUpdateCoordinator]

@dataclass
class IndiAllSkyData:
    exposure: ExposureData | None = ...
    latest_keogram: MediaData | None = ...
    latest_startrail: MediaData | None = ...
    sensor: SensorData | None = ...

class IndiAllSkyDataUpdateCoordinator(DataUpdateCoordinator[IndiAllSkyData]):
    client: Incomplete
    latest_exposure: ExposureData | None
    latest_keogram: MediaData | None
    latest_startrail: MediaData | None
    latest_sensor: SensorData | None
    def __init__(self, hass: HomeAssistant, entry: IndiAllSkyConfigEntry) -> None: ...
    def _handle_exposure_complete(self, exposure: ExposureData) -> None: ...
    def _handle_keogram_complete(self, media: MediaData) -> None: ...
    def _handle_startrail_complete(self, media: MediaData) -> None: ...
    def _handle_sensor_update(self, sensor: SensorData) -> None: ...
    @override
    async def _async_update_data(self) -> IndiAllSkyData: ...
