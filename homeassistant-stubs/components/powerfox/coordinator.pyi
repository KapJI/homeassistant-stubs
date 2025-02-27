from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from powerfox import Device as Device, Powerfox as Powerfox, Poweropti

type PowerfoxConfigEntry = ConfigEntry[list[PowerfoxDataUpdateCoordinator]]
class PowerfoxDataUpdateCoordinator(DataUpdateCoordinator[Poweropti]):
    config_entry: PowerfoxConfigEntry
    client: Incomplete
    device: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: PowerfoxConfigEntry, client: Powerfox, device: Device) -> None: ...
    async def _async_update_data(self) -> Poweropti: ...
