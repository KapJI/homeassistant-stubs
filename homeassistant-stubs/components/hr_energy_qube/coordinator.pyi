from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from python_qube_heatpump import QubeClient as QubeClient
from python_qube_heatpump.models import QubeState

_LOGGER: Incomplete

class QubeCoordinator(DataUpdateCoordinator[QubeState]):
    client: Incomplete
    def __init__(self, hass: HomeAssistant, client: QubeClient, entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> QubeState: ...
