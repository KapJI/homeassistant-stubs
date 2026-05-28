from .const import DOMAIN as DOMAIN, ValveDeviceClass as ValveDeviceClass, ValveEntityFeature as ValveEntityFeature, ValveState as ValveState
from .entity import ATTR_CURRENT_POSITION as ATTR_CURRENT_POSITION, ATTR_IS_CLOSED as ATTR_IS_CLOSED, ValveEntity as ValveEntity, ValveEntityDescription as ValveEntityDescription
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SERVICE_CLOSE_VALVE as SERVICE_CLOSE_VALVE, SERVICE_OPEN_VALVE as SERVICE_OPEN_VALVE, SERVICE_SET_VALVE_POSITION as SERVICE_SET_VALVE_POSITION, SERVICE_STOP_VALVE as SERVICE_STOP_VALVE, SERVICE_TOGGLE as SERVICE_TOGGLE, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey

_LOGGER: Incomplete
DATA_COMPONENT: HassKey[EntityComponent[ValveEntity]]
ENTITY_ID_FORMAT: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete
SCAN_INTERVAL: Incomplete
DEVICE_CLASSES_SCHEMA: Incomplete
ATTR_POSITION: str

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
