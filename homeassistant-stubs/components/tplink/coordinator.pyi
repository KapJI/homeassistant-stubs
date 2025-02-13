from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from kasa import Credentials as Credentials, Device as Device

_LOGGER: Incomplete

@dataclass(slots=True)
class TPLinkData:
    parent_coordinator: TPLinkDataUpdateCoordinator
    camera_credentials: Credentials | None
    live_view: bool | None
type TPLinkConfigEntry = ConfigEntry[TPLinkData]

REQUEST_REFRESH_DELAY: float

class TPLinkDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: TPLinkConfigEntry
    device: Incomplete
    _update_children: Incomplete
    _previous_child_device_ids: Incomplete
    removed_child_device_ids: set[str]
    _child_coordinators: dict[str, TPLinkDataUpdateCoordinator]
    def __init__(self, hass: HomeAssistant, device: Device, update_interval: timedelta, config_entry: TPLinkConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...
    async def _process_child_devices(self) -> None: ...
    def get_child_coordinator(self, child: Device, platform_domain: str) -> TPLinkDataUpdateCoordinator: ...
