from .const import CONF_BALANCING_AUTHORITY_ABBREV as CONF_BALANCING_AUTHORITY_ABBREV, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aiowatttime import Client as Client
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import override

DEFAULT_UPDATE_INTERVAL: Incomplete
type WattTimeData = dict[str, StateType]
type WattTimeConfigEntry = ConfigEntry[WattTimeCoordinator]

class WattTimeCoordinator(DataUpdateCoordinator[WattTimeData]):
    config_entry: WattTimeConfigEntry
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: WattTimeConfigEntry, client: Client) -> None: ...
    @override
    async def _async_update_data(self) -> WattTimeData: ...
