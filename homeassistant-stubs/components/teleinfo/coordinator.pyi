from .const import CONF_SERIAL_PORT as CONF_SERIAL_PORT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete
type TeleinfoConfigEntry = ConfigEntry[TeleinfoCoordinator]

class TeleinfoCoordinator(DataUpdateCoordinator[dict[str, str]]):
    config_entry: TeleinfoConfigEntry
    def __init__(self, hass: HomeAssistant, entry: TeleinfoConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, str]: ...
