from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioharmanluxury import DeviceInfo as DeviceInfo, HarmanLuxuryClient as HarmanLuxuryClient, HarmanLuxuryState
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

_LOGGER: Incomplete
type HarmanLuxuryConfigEntry = ConfigEntry[HarmanLuxuryCoordinator]
_SCAN_INTERVAL: Incomplete

class HarmanLuxuryCoordinator(DataUpdateCoordinator[HarmanLuxuryState]):
    config_entry: HarmanLuxuryConfigEntry
    device_info: DeviceInfo
    position_updated_at: datetime | None
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HarmanLuxuryConfigEntry, client: HarmanLuxuryClient) -> None: ...
    @override
    async def _async_setup(self) -> None: ...
    @override
    async def _async_update_data(self) -> HarmanLuxuryState: ...
