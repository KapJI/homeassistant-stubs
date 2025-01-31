import pyevilgenius
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

UPDATE_INTERVAL: int
_LOGGER: Incomplete
type EvilGeniusConfigEntry = ConfigEntry[EvilGeniusUpdateCoordinator]

class EvilGeniusUpdateCoordinator(DataUpdateCoordinator[dict]):
    info: dict
    product: dict | None
    client: Incomplete
    def __init__(self, hass: HomeAssistant, entry: EvilGeniusConfigEntry, client: pyevilgenius.EvilGeniusDevice) -> None: ...
    @property
    def device_name(self) -> str: ...
    @property
    def product_name(self) -> str | None: ...
    async def _async_update_data(self) -> dict: ...
