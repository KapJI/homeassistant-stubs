from .const import CONF_KAMEREON_ACCOUNT_ID as CONF_KAMEREON_ACCOUNT_ID, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from renault_api.renault_account import RenaultAccount as RenaultAccount
from typing import Any

LOGGER: Any

class RenaultHub:
    _hass: Any
    _client: Any
    _account: Any
    _vehicles: Any
    def __init__(self, hass: HomeAssistant, locale: str) -> None: ...
    async def attempt_login(self, username: str, password: str) -> bool: ...
    async def async_initialise(self, config_entry: ConfigEntry) -> None: ...
    async def get_account_ids(self) -> list[str]: ...
    @property
    def vehicles(self) -> dict[str, RenaultVehicleProxy]: ...
