import logging
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete

class IdasenDeskCoordinator(DataUpdateCoordinator[int | None]):
    _address: Incomplete
    _expected_connected: bool
    _connection_lost: bool
    _disconnect_lock: Incomplete
    desk: Incomplete
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, name: str, address: str) -> None: ...
    async def async_connect(self) -> bool: ...
    async def async_disconnect(self) -> None: ...
    async def async_ensure_connection_state(self) -> None: ...
    def async_set_updated_data(self, data: int | None) -> None: ...
