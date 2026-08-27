from .const import CONF_APPS as CONF_APPS, CONF_DEVICE_TYPE as CONF_DEVICE_TYPE, CONF_VOLUME_STEP as CONF_VOLUME_STEP, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN, VIZIO_DEVICE_CLASSES as VIZIO_DEVICE_CLASSES
from .coordinator import VizioAppsDataUpdateCoordinator as VizioAppsDataUpdateCoordinator, VizioConfigEntry as VizioConfigEntry, VizioDeviceCoordinator as VizioDeviceCoordinator, VizioRuntimeData as VizioRuntimeData
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_EXCLUDE as CONF_EXCLUDE, CONF_HOST as CONF_HOST, CONF_INCLUDE as CONF_INCLUDE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from vizaio import DeviceType

DATA_APPS: HassKey[VizioAppsDataUpdateCoordinator]
CONFIG_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: VizioConfigEntry) -> bool: ...
async def _async_resolve_device_type(hass: HomeAssistant, entry: VizioConfigEntry) -> DeviceType: ...
async def async_setup_entry(hass: HomeAssistant, entry: VizioConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VizioConfigEntry) -> bool: ...
