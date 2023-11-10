from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from starlink_grpc import AlertDict as AlertDict, LocationDict as LocationDict, ObstructionDict as ObstructionDict, StatusDict as StatusDict

_LOGGER: Incomplete

@dataclass
class StarlinkData:
    location: LocationDict
    status: StatusDict
    obstruction: ObstructionDict
    alert: AlertDict
    def __init__(self, location, status, obstruction, alert) -> None: ...

class StarlinkUpdateCoordinator(DataUpdateCoordinator[StarlinkData]):
    channel_context: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, url: str) -> None: ...
    async def _async_update_data(self) -> StarlinkData: ...
    async def async_stow_starlink(self, stow: bool) -> None: ...
    async def async_reboot_starlink(self) -> None: ...
