from _typeshed import Incomplete
from genie_partner_sdk.client import AladdinConnectClient as AladdinConnectClient
from genie_partner_sdk.model import GarageDoor
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
type AladdinConnectConfigEntry = ConfigEntry[dict[str, AladdinConnectCoordinator]]
SCAN_INTERVAL: Incomplete

class AladdinConnectCoordinator(DataUpdateCoordinator[GarageDoor]):
    client: Incomplete
    data: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AladdinConnectConfigEntry, client: AladdinConnectClient, garage_door: GarageDoor) -> None: ...
    async def _async_update_data(self) -> GarageDoor: ...
