from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from energieleser import EnergieleserClient as EnergieleserClient, EnergieleserDevice
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

SCAN_INTERVAL: Incomplete
type EnergieleserConfigEntry = ConfigEntry[EnergieleserCoordinator]

class EnergieleserCoordinator(DataUpdateCoordinator[EnergieleserDevice]):
    config_entry: EnergieleserConfigEntry
    client: Incomplete
    device_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: EnergieleserConfigEntry, client: EnergieleserClient) -> None: ...
    @override
    async def _async_update_data(self) -> EnergieleserDevice: ...
