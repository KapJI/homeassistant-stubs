from .common import SynoApi as SynoApi, raise_config_entry_auth_error as raise_config_entry_auth_error
from .const import CONF_BACKUP_PATH as CONF_BACKUP_PATH, CONF_BACKUP_SHARE as CONF_BACKUP_SHARE, DATA_BACKUP_AGENT_LISTENERS as DATA_BACKUP_AGENT_LISTENERS, DEFAULT_VERIFY_SSL as DEFAULT_VERIFY_SSL, DOMAIN as DOMAIN, EXCEPTION_DETAILS as EXCEPTION_DETAILS, EXCEPTION_UNKNOWN as EXCEPTION_UNKNOWN, PLATFORMS as PLATFORMS, SYNOLOGY_AUTH_FAILED_EXCEPTIONS as SYNOLOGY_AUTH_FAILED_EXCEPTIONS, SYNOLOGY_CONNECTION_EXCEPTIONS as SYNOLOGY_CONNECTION_EXCEPTIONS
from .coordinator import SynologyDSMCameraUpdateCoordinator as SynologyDSMCameraUpdateCoordinator, SynologyDSMCentralUpdateCoordinator as SynologyDSMCentralUpdateCoordinator, SynologyDSMConfigEntry as SynologyDSMConfigEntry, SynologyDSMData as SynologyDSMData, SynologyDSMSwitchUpdateCoordinator as SynologyDSMSwitchUpdateCoordinator
from .service import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_MAC as CONF_MAC, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_VERIFY_SSL as CONF_VERIFY_SSL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from synology_dsm.api.surveillance_station.camera import SynoCamera as SynoCamera

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SynologyDSMConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SynologyDSMConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: SynologyDSMConfigEntry) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: SynologyDSMConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
