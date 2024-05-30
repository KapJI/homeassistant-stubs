from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, MAX_RETRIES_AFTER_STARTUP as MAX_RETRIES_AFTER_STARTUP
from _typeshed import Incomplete
from airthings_ble import AirthingsDevice
from homeassistant.components import bluetooth as bluetooth
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM

PLATFORMS: list[Platform]
_LOGGER: Incomplete
AirthingsBLEDataUpdateCoordinator = DataUpdateCoordinator[AirthingsDevice]
AirthingsBLEConfigEntry = ConfigEntry[AirthingsBLEDataUpdateCoordinator]

async def async_setup_entry(hass: HomeAssistant, entry: AirthingsBLEConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AirthingsBLEConfigEntry) -> bool: ...
