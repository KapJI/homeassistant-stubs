from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util import Throttle as Throttle
from pybotvac import Account as Account
from typing import Any
from urllib3.response import HTTPResponse

_LOGGER: Incomplete

class NeatoHub:
    _hass: Incomplete
    my_neato: Account
    robots: set[Any]
    persistent_maps: dict[str, Any]
    map_data: dict[str, Any]
    def __init__(self, hass: HomeAssistant, neato: Account) -> None: ...
    def update_robots(self) -> None: ...
    def download_map(self, url: str) -> HTTPResponse: ...
    async def async_update_entry_unique_id(self, entry: ConfigEntry) -> str: ...
