from .const import CONF_ADVANCED as CONF_ADVANCED, CONF_AUTH as CONF_AUTH, CONF_ENCODING as CONF_ENCODING, CONF_INDEX as CONF_INDEX, CONF_SELECT as CONF_SELECT, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import ScrapeCoordinator as ScrapeCoordinator
from _typeshed import Incomplete
from homeassistant.components.rest import RESOURCE_SCHEMA as RESOURCE_SCHEMA, create_rest_data_from_config as create_rest_data_from_config
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_ATTRIBUTE as CONF_ATTRIBUTE, CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_HEADERS as CONF_HEADERS, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_TIMEOUT as CONF_TIMEOUT, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_USERNAME as CONF_USERNAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr, discovery as discovery
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY, TEMPLATE_SENSOR_BASE_SCHEMA as TEMPLATE_SENSOR_BASE_SCHEMA, ValueTemplate as ValueTemplate
from homeassistant.helpers.typing import ConfigType as ConfigType

type ScrapeConfigEntry = ConfigEntry[ScrapeCoordinator]
_LOGGER: Incomplete
SENSOR_SCHEMA: Incomplete
COMBINED_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ScrapeConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ScrapeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ScrapeConfigEntry) -> bool: ...
async def update_listener(hass: HomeAssistant, entry: ScrapeConfigEntry) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, entry: ConfigEntry, device: dr.DeviceEntry) -> bool: ...
