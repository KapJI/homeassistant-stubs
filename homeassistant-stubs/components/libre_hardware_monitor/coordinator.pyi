from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from librehardwaremonitor_api.model import DeviceId, DeviceName, LibreHardwareMonitorData

_LOGGER: Incomplete
type LibreHardwareMonitorConfigEntry = ConfigEntry[LibreHardwareMonitorCoordinator]

class LibreHardwareMonitorCoordinator(DataUpdateCoordinator[LibreHardwareMonitorData]):
    config_entry: LibreHardwareMonitorConfigEntry
    _api: Incomplete
    _previous_devices: dict[DeviceId, DeviceName]
    def __init__(self, hass: HomeAssistant, config_entry: LibreHardwareMonitorConfigEntry) -> None: ...
    async def _async_update_data(self) -> LibreHardwareMonitorData: ...
    async def _async_refresh(self, log_failures: bool = True, raise_on_auth_failed: bool = False, scheduled: bool = False, raise_on_entry_error: bool = False) -> None: ...
    async def _async_handle_changes_in_devices(self, detected_devices: dict[DeviceId, DeviceName]) -> None: ...
