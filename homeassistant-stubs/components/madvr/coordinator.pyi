from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from madvr.madvr import Madvr as Madvr
from typing import Any

_LOGGER: Incomplete
type MadVRConfigEntry = ConfigEntry[MadVRCoordinator]

class MadVRCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: MadVRConfigEntry
    mac: Incomplete
    client: Incomplete
    data: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: MadVRConfigEntry, client: Madvr) -> None: ...
    def handle_push_data(self, data: dict[str, Any]) -> None: ...
    async def handle_coordinator_load(self) -> None: ...
