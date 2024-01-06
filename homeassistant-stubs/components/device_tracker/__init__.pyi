from .config_entry import ScannerEntity as ScannerEntity, TrackerEntity as TrackerEntity, async_setup_entry as async_setup_entry, async_unload_entry as async_unload_entry
from .const import ATTR_ATTRIBUTES as ATTR_ATTRIBUTES, ATTR_BATTERY as ATTR_BATTERY, ATTR_DEV_ID as ATTR_DEV_ID, ATTR_GPS as ATTR_GPS, ATTR_HOST_NAME as ATTR_HOST_NAME, ATTR_IP as ATTR_IP, ATTR_LOCATION_NAME as ATTR_LOCATION_NAME, ATTR_MAC as ATTR_MAC, ATTR_SOURCE_TYPE as ATTR_SOURCE_TYPE, CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, CONF_NEW_DEVICE_DEFAULTS as CONF_NEW_DEVICE_DEFAULTS, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_TRACK_NEW as CONF_TRACK_NEW, CONNECTED_DEVICE_REGISTERED as CONNECTED_DEVICE_REGISTERED, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME, DEFAULT_TRACK_NEW as DEFAULT_TRACK_NEW, DOMAIN as DOMAIN, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, SCAN_INTERVAL as SCAN_INTERVAL, SourceType as SourceType, _DEPRECATED_SOURCE_TYPE_BLUETOOTH as _DEPRECATED_SOURCE_TYPE_BLUETOOTH, _DEPRECATED_SOURCE_TYPE_BLUETOOTH_LE as _DEPRECATED_SOURCE_TYPE_BLUETOOTH_LE, _DEPRECATED_SOURCE_TYPE_GPS as _DEPRECATED_SOURCE_TYPE_GPS, _DEPRECATED_SOURCE_TYPE_ROUTER as _DEPRECATED_SOURCE_TYPE_ROUTER
from .legacy import AsyncSeeCallback as AsyncSeeCallback, DeviceScanner as DeviceScanner, PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE, SERVICE_SEE as SERVICE_SEE, SERVICE_SEE_PAYLOAD_SCHEMA as SERVICE_SEE_PAYLOAD_SCHEMA, SOURCE_TYPES as SOURCE_TYPES, SeeCallback as SeeCallback, see as see
from _typeshed import Incomplete
from homeassistant.const import ATTR_GPS_ACCURACY as ATTR_GPS_ACCURACY, STATE_HOME as STATE_HOME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.deprecation import all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass

def is_on(hass: HomeAssistant, entity_id: str) -> bool: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
