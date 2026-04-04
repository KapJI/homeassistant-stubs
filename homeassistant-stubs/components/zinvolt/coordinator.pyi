from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from zinvolt import ZinvoltClient as ZinvoltClient
from zinvolt.models import Battery as Battery, BatteryState as BatteryState, Unit as Unit

_LOGGER: Incomplete
type ZinvoltConfigEntry = ConfigEntry[dict[str, ZinvoltDeviceCoordinator]]

@dataclass
class ZinvoltData:
    battery: BatteryState
    batteries: dict[str, BatteryData]

@dataclass
class BatteryData:
    sw_version: str
    model: str
    points: dict[str, bool]

class ZinvoltDeviceCoordinator(DataUpdateCoordinator[ZinvoltData]):
    battery_units: dict[str, Unit]
    battery: Incomplete
    client: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: ZinvoltConfigEntry, client: ZinvoltClient, battery: Battery) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> ZinvoltData: ...
