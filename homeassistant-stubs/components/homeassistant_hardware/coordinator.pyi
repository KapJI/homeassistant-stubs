from _typeshed import Incomplete
from aiohttp import ClientSession as ClientSession
from ha_silabs_firmware_client import FirmwareManifest
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
FIRMWARE_REFRESH_INTERVAL: Incomplete

class FirmwareUpdateCoordinator(DataUpdateCoordinator[FirmwareManifest]):
    hass: Incomplete
    session: Incomplete
    client: Incomplete
    def __init__(self, hass: HomeAssistant, session: ClientSession, url: str) -> None: ...
    async def _async_update_data(self) -> FirmwareManifest: ...
