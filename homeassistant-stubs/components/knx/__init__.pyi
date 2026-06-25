from .const import CONF_KNX_DEFAULT_RATE_LIMIT as CONF_KNX_DEFAULT_RATE_LIMIT, CONF_KNX_DEFAULT_STATE_UPDATER as CONF_KNX_DEFAULT_STATE_UPDATER, CONF_KNX_EXPOSE as CONF_KNX_EXPOSE, CONF_KNX_KNXKEY_FILENAME as CONF_KNX_KNXKEY_FILENAME, CONF_KNX_RATE_LIMIT as CONF_KNX_RATE_LIMIT, CONF_KNX_STATE_UPDATER as CONF_KNX_STATE_UPDATER, CONF_KNX_TELEGRAM_DB_LOAD_HOURS as CONF_KNX_TELEGRAM_DB_LOAD_HOURS, CONF_KNX_TELEGRAM_DB_RETENTION_DAYS as CONF_KNX_TELEGRAM_DB_RETENTION_DAYS, DATA_HASS_CONFIG as DATA_HASS_CONFIG, DOMAIN as DOMAIN, KNX_MODULE_KEY as KNX_MODULE_KEY, KNX_TELEGRAM_DB_PATH_SQLITE as KNX_TELEGRAM_DB_PATH_SQLITE, KNX_TELEGRAM_DB_RETENTION_DEFAULT as KNX_TELEGRAM_DB_RETENTION_DEFAULT, KNX_TELEGRAM_LOAD_HOURS_DEFAULT as KNX_TELEGRAM_LOAD_HOURS_DEFAULT, SUPPORTED_PLATFORMS_UI as SUPPORTED_PLATFORMS_UI, SUPPORTED_PLATFORMS_YAML as SUPPORTED_PLATFORMS_YAML
from .expose import create_combined_knx_exposure as create_combined_knx_exposure
from .knx_module import KNXModule as KNXModule
from .schema import BinarySensorSchema as BinarySensorSchema, ButtonSchema as ButtonSchema, ClimateSchema as ClimateSchema, CoverSchema as CoverSchema, DateSchema as DateSchema, DateTimeSchema as DateTimeSchema, EventSchema as EventSchema, ExposeSchema as ExposeSchema, FanSchema as FanSchema, LightSchema as LightSchema, NotifySchema as NotifySchema, NumberSchema as NumberSchema, SceneSchema as SceneSchema, SelectSchema as SelectSchema, SensorSchema as SensorSchema, SwitchSchema as SwitchSchema, TextSchema as TextSchema, TimeSchema as TimeSchema, WeatherSchema as WeatherSchema
from .services import async_setup_services as async_setup_services
from .websocket import register_panel as register_panel
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.reload import async_integration_yaml_config as async_integration_yaml_config
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

_KNX_YAML_CONFIG: Final[str]
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry) -> bool: ...
