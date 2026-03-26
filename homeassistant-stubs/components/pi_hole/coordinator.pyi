from .const import MIN_TIME_BETWEEN_UPDATES as MIN_TIME_BETWEEN_UPDATES, VERSION_6_RESPONSE_TO_5_ERROR as VERSION_6_RESPONSE_TO_5_ERROR
from _typeshed import Incomplete
from dataclasses import dataclass
from hole import HoleV5 as HoleV5, HoleV6 as HoleV6
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete

@dataclass
class PiHoleData:
    api: HoleV5 | HoleV6
    coordinator: PiHoleUpdateCoordinator
    api_version: int
type PiHoleConfigEntry = ConfigEntry[PiHoleData]

class PiHoleUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: PiHoleConfigEntry
    _api: Incomplete
    _name: Incomplete
    _host: Incomplete
    def __init__(self, hass: HomeAssistant, api: HoleV5 | HoleV6, config_entry: PiHoleConfigEntry) -> None: ...
    async def _async_update_data(self) -> None: ...
