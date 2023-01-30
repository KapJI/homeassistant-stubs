from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from goalzero import Yeti as Yeti
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

class GoalZeroDataUpdateCoordinator(DataUpdateCoordinator[None]):
    config_entry: ConfigEntry
    api: Incomplete
    def __init__(self, hass: HomeAssistant, api: Yeti) -> None: ...
    async def _async_update_data(self) -> None: ...
