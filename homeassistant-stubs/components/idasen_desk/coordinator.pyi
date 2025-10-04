from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
type IdasenDeskConfigEntry = ConfigEntry[IdasenDeskCoordinator]
UPDATE_DEBOUNCE_TIME: float

class IdasenDeskCoordinator(DataUpdateCoordinator[int | None]):
    config_entry: IdasenDeskConfigEntry
    address: Incomplete
    desk: Incomplete
    _expected_connected: bool
    _height: int | None
    _debouncer: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: IdasenDeskConfigEntry, address: str) -> None: ...
    async def async_connect(self) -> bool: ...
    async def async_disconnect(self) -> None: ...
    async def async_connect_if_expected(self) -> None: ...
    @callback
    def _async_handle_update(self, height: int | None) -> None: ...
