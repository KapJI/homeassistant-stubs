from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.dt import now as now
from pydrawise import Hydrawise as Hydrawise
from pydrawise.schema import Controller as Controller, ControllerWaterUseSummary as ControllerWaterUseSummary, Sensor as Sensor, User as User, Zone as Zone

@dataclass
class HydrawiseData:
    user: User
    controllers: dict[int, Controller]
    zones: dict[int, Zone]
    sensors: dict[int, Sensor]
    daily_water_summary: dict[int, ControllerWaterUseSummary]
    def __init__(self, user, controllers, zones, sensors, daily_water_summary) -> None: ...

class HydrawiseDataUpdateCoordinator(DataUpdateCoordinator[HydrawiseData]):
    api: Hydrawise
    def __init__(self, hass: HomeAssistant, api: Hydrawise, scan_interval: timedelta) -> None: ...
    async def _async_update_data(self) -> HydrawiseData: ...
