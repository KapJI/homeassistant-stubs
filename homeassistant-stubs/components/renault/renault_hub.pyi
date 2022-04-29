from .const import CONF_KAMEREON_ACCOUNT_ID as CONF_KAMEREON_ACCOUNT_ID, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_IDENTIFIERS as ATTR_IDENTIFIERS, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, ATTR_SW_VERSION as ATTR_SW_VERSION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from renault_api.kamereon.models import KamereonVehiclesLink as KamereonVehiclesLink
from renault_api.renault_account import RenaultAccount as RenaultAccount

LOGGER: Incomplete

class RenaultHub:
    _hass: Incomplete
    _client: Incomplete
    _account: Incomplete
    _vehicles: Incomplete
    def __init__(self, hass: HomeAssistant, locale: str) -> None: ...
    async def attempt_login(self, username: str, password: str) -> bool: ...
    async def async_initialise(self, config_entry: ConfigEntry) -> None: ...
    async def async_initialise_vehicle(self, vehicle_link: KamereonVehiclesLink, renault_account: RenaultAccount, scan_interval: timedelta, config_entry: ConfigEntry, device_registry: dr.DeviceRegistry) -> None: ...
    async def get_account_ids(self) -> list[str]: ...
    @property
    def vehicles(self) -> dict[str, RenaultVehicleProxy]: ...
