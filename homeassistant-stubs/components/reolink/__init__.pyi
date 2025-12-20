from .const import BATTERY_PASSIVE_WAKE_UPDATE_INTERVAL as BATTERY_PASSIVE_WAKE_UPDATE_INTERVAL, CONF_BC_ONLY as CONF_BC_ONLY, CONF_BC_PORT as CONF_BC_PORT, CONF_FIRMWARE_CHECK_TIME as CONF_FIRMWARE_CHECK_TIME, CONF_SUPPORTS_PRIVACY_MODE as CONF_SUPPORTS_PRIVACY_MODE, CONF_USE_HTTPS as CONF_USE_HTTPS, DOMAIN as DOMAIN
from .exceptions import PasswordIncompatible as PasswordIncompatible, ReolinkException as ReolinkException, UserNotAdmin as UserNotAdmin
from .host import ReolinkHost as ReolinkHost
from .services import async_setup_services as async_setup_services
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData, get_device_uid_and_ch as get_device_uid_and_ch, get_store as get_store
from .views import PlaybackProxyView as PlaybackProxyView
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

_LOGGER: Incomplete
PLATFORMS: Incomplete
DEVICE_UPDATE_INTERVAL_MIN: Incomplete
DEVICE_UPDATE_INTERVAL_PER_CAM: Incomplete
FIRMWARE_UPDATE_INTERVAL: Incomplete
NUM_CRED_ERRORS: int
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry) -> bool: ...
async def register_callbacks(host: ReolinkHost, device_coordinator: DataUpdateCoordinator[None], hass: HomeAssistant) -> None: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ReolinkConfigEntry, device: dr.DeviceEntry) -> bool: ...
def migrate_entity_ids(hass: HomeAssistant, config_entry_id: str, host: ReolinkHost) -> None: ...
