from .const import ATTRIBUTION as ATTRIBUTION, CONF_ACCOUNT as CONF_ACCOUNT, CONF_READ_ONLY as CONF_READ_ONLY, DATA_ENTRIES as DATA_ENTRIES, DATA_HASS_CONFIG as DATA_HASS_CONFIG
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_REGION as CONF_REGION, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as device_registry, discovery as discovery
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.event import track_utc_time_change as track_utc_time_change
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util import slugify as slugify
from typing import Any

_LOGGER: Any
DOMAIN: str
ATTR_VIN: str
CONFIG_SCHEMA: Any
SERVICE_SCHEMA: Any
DEFAULT_OPTIONS: Any
PLATFORMS: Any
UPDATE_INTERVAL: int
SERVICE_UPDATE_STATE: str
_SERVICE_MAP: Any
UNDO_UPDATE_LISTENER: str

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _async_migrate_options_from_data_if_missing(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
def setup_account(entry: ConfigEntry, hass: HomeAssistant, name: str) -> BMWConnectedDriveAccount: ...

class BMWConnectedDriveAccount:
    read_only: Any
    account: Any
    name: Any
    _update_listeners: Any
    def __init__(self, username: str, password: str, region_str: str, name: str, read_only: bool, lat: Union[float, None] = ..., lon: Union[float, None] = ...) -> None: ...
    def update(self, *_: Any) -> None: ...
    def add_update_listener(self, listener: Callable[[], None]) -> None: ...

class BMWConnectedDriveBaseEntity(Entity):
    _attr_should_poll: bool
    _attr_attribution: Any
    _account: Any
    _vehicle: Any
    _attrs: Any
    _attr_device_info: Any
    def __init__(self, account: BMWConnectedDriveAccount, vehicle: ConnectedDriveVehicle) -> None: ...
    def update_callback(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
