from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from python_qube_heatpump import QubeClient as QubeClient
from python_qube_heatpump.models import QubeState as QubeState

_LOGGER: Incomplete

@dataclass
class QubeData:
    state: QubeState
    switches: dict[str, bool | None]

class QubeCoordinator(DataUpdateCoordinator[QubeData]):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: QubeClient, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> QubeData: ...
