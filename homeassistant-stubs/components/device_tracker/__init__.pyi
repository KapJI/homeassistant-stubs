from .const import ATTR_ATTRIBUTES as ATTR_ATTRIBUTES, ATTR_BATTERY as ATTR_BATTERY, ATTR_DEV_ID as ATTR_DEV_ID, ATTR_GPS as ATTR_GPS, ATTR_HOST_NAME as ATTR_HOST_NAME, ATTR_IN_ZONES as ATTR_IN_ZONES, ATTR_IP as ATTR_IP, ATTR_LOCATION_NAME as ATTR_LOCATION_NAME, ATTR_MAC as ATTR_MAC, ATTR_SOURCE_TYPE as ATTR_SOURCE_TYPE, CONF_ASSOCIATED_ZONE as CONF_ASSOCIATED_ZONE, CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, CONF_NEW_DEVICE_DEFAULTS as CONF_NEW_DEVICE_DEFAULTS, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_TRACK_NEW as CONF_TRACK_NEW, CONNECTED_DEVICE_REGISTERED as CONNECTED_DEVICE_REGISTERED, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME, DEFAULT_TRACK_NEW as DEFAULT_TRACK_NEW, DOMAIN as DOMAIN, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, LOGGER as LOGGER, PLATFORM_TYPE_LEGACY as PLATFORM_TYPE_LEGACY, SCAN_INTERVAL as SCAN_INTERVAL, SourceType as SourceType
from .entity import BaseScannerEntity as BaseScannerEntity, BaseTrackerEntity as BaseTrackerEntity, ScannerEntity as ScannerEntity, ScannerEntityDescription as ScannerEntityDescription, TrackerEntity as TrackerEntity, TrackerEntityDescription as TrackerEntityDescription
from .legacy import AsyncSeeCallback as AsyncSeeCallback, DeviceScanner as DeviceScanner, DeviceTracker as DeviceTracker, PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, SERVICE_SEE as SERVICE_SEE, SERVICE_SEE_PAYLOAD_SCHEMA as SERVICE_SEE_PAYLOAD_SCHEMA, SOURCE_TYPES as SOURCE_TYPES, SeeCallback as SeeCallback, async_create_platform_type as async_create_platform_type, see as see
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_HOME as STATE_HOME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey

DATA_COMPONENT: HassKey[EntityComponent[BaseTrackerEntity]]

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
