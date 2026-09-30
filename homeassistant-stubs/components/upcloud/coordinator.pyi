import upcloud_api
from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import override

_LOGGER: Incomplete
type UpCloudConfigEntry = ConfigEntry[UpCloudDataUpdateCoordinator]

class UpCloudDataUpdateCoordinator(DataUpdateCoordinator[dict[str, upcloud_api.Server]]):
    cloud_manager: Incomplete
    def __init__(self, hass: HomeAssistant, *, config_entry: UpCloudConfigEntry, cloud_manager: upcloud_api.CloudManager, username: str) -> None: ...
    @override
    async def _async_update_data(self) -> dict[str, upcloud_api.Server]: ...
