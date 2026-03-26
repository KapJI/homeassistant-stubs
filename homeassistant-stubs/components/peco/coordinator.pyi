from .const import CONF_COUNTY as CONF_COUNTY, LOGGER as LOGGER, OUTAGE_SCAN_INTERVAL as OUTAGE_SCAN_INTERVAL, SMART_METER_SCAN_INTERVAL as SMART_METER_SCAN_INTERVAL
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from peco import AlertResults as AlertResults, OutageResults as OutageResults

@dataclass
class PECOCoordinatorData:
    outages: OutageResults
    alerts: AlertResults

class PecoOutageCoordinator(DataUpdateCoordinator[PECOCoordinatorData]):
    config_entry: ConfigEntry
    _api: Incomplete
    _websession: Incomplete
    _county: str
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> PECOCoordinatorData: ...

class PecoSmartMeterCoordinator(DataUpdateCoordinator[bool]):
    config_entry: ConfigEntry
    _api: Incomplete
    _websession: Incomplete
    _phone_number: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, phone_number: str) -> None: ...
    async def _async_update_data(self) -> bool: ...
