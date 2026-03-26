from _typeshed import Incomplete
from genie_partner_sdk.client import AladdinConnectClient as AladdinConnectClient
from genie_partner_sdk.model import GarageDoor
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
type AladdinConnectConfigEntry = ConfigEntry[AladdinConnectCoordinator]
SCAN_INTERVAL: Incomplete

class AladdinConnectCoordinator(DataUpdateCoordinator[dict[str, GarageDoor]]):
    config_entry: AladdinConnectConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: AladdinConnectConfigEntry, client: AladdinConnectClient) -> None: ...
    async def _async_update_data(self) -> dict[str, GarageDoor]: ...
