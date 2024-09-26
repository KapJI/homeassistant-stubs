from .const import SENSOR_UPDATE_INTERVAL as SENSOR_UPDATE_INTERVAL, STATUS_API_TIMEOUT as STATUS_API_TIMEOUT, STATUS_SENSOR_LASTSCAN as STATUS_SENSOR_LASTSCAN, STATUS_SENSOR_NEEDSRESTART as STATUS_SENSOR_NEEDSRESTART, STATUS_SENSOR_RESCAN as STATUS_SENSOR_RESCAN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysqueezebox import Server as Server

_LOGGER: Incomplete

class LMSStatusDataUpdateCoordinator(DataUpdateCoordinator):
    lms: Incomplete
    newversion_regex: Incomplete
    def __init__(self, hass: HomeAssistant, lms: Server) -> None: ...
    async def _async_update_data(self) -> dict: ...
    def _prepare_status_data(self, data: dict) -> dict: ...
