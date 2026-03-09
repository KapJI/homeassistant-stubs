from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from zinvolt import ZinvoltClient as ZinvoltClient
from zinvolt.models import Battery as Battery, BatteryState

_LOGGER: Incomplete
type ZinvoltConfigEntry = ConfigEntry[dict[str, ZinvoltDeviceCoordinator]]

class ZinvoltDeviceCoordinator(DataUpdateCoordinator[BatteryState]):
    battery: Incomplete
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ZinvoltConfigEntry, client: ZinvoltClient, battery: Battery) -> None: ...
    async def _async_update_data(self) -> BatteryState: ...
