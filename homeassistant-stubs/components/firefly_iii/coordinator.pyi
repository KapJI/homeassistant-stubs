from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_URL as CONF_URL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyfirefly.models import Account as Account, Bill as Bill, Budget as Budget, Category as Category, Currency as Currency

_LOGGER: Incomplete
type FireflyConfigEntry = ConfigEntry[FireflyDataUpdateCoordinator]
DEFAULT_SCAN_INTERVAL: Incomplete

@dataclass
class FireflyCoordinatorData:
    accounts: list[Account]
    categories: list[Category]
    category_details: list[Category]
    budgets: list[Budget]
    bills: list[Bill]
    primary_currency: Currency

class FireflyDataUpdateCoordinator(DataUpdateCoordinator[FireflyCoordinatorData]):
    config_entry: FireflyConfigEntry
    firefly: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: FireflyConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> FireflyCoordinatorData: ...
