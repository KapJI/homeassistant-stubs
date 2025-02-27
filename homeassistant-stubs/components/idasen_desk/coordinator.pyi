from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
type IdasenDeskConfigEntry = ConfigEntry[IdasenDeskCoordinator]

class IdasenDeskCoordinator(DataUpdateCoordinator[int | None]):
    config_entry: IdasenDeskConfigEntry
    address: Incomplete
    _expected_connected: bool
    desk: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: IdasenDeskConfigEntry, address: str) -> None: ...
    async def async_connect(self) -> bool: ...
    async def async_disconnect(self) -> None: ...
    async def async_connect_if_expected(self) -> None: ...
