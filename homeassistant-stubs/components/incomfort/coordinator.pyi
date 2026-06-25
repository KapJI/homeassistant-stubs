from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from incomfortclient import Gateway as InComfortGateway, Heater as InComfortHeater
from typing import override

type InComfortConfigEntry = ConfigEntry[InComfortDataCoordinator]
_LOGGER: Incomplete
UPDATE_INTERVAL: int

@dataclass
class InComfortData:
    client: InComfortGateway
    heaters: list[InComfortHeater] = field(default_factory=list)

@callback
def async_cleanup_stale_devices(hass: HomeAssistant, entry: InComfortConfigEntry, data: InComfortData, gateway_device: dr.DeviceEntry) -> None: ...

class InComfortDataCoordinator(DataUpdateCoordinator[InComfortData]):
    config_entry: InComfortConfigEntry
    client: Incomplete
    unique_id: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: InComfortConfigEntry, client: InComfortGateway) -> None: ...
    @override
    async def _async_update_data(self) -> InComfortData: ...
