from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

STATE_FIRST_QUARTER: str
STATE_FULL_MOON: str
STATE_LAST_QUARTER: str
STATE_NEW_MOON: str
STATE_WANING_CRESCENT: str
STATE_WANING_GIBBOUS: str
STATE_WAXING_GIBBOUS: str
STATE_WAXING_CRESCENT: str
MOON_ICONS: Any
PLATFORM_SCHEMA: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MoonSensorEntity(SensorEntity):
    _attr_device_class: str
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, entry: ConfigEntry) -> None: ...
    _attr_native_value: Any
    _attr_icon: Any
    async def async_update(self) -> None: ...
