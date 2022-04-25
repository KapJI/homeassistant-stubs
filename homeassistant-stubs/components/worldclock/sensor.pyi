from datetime import tzinfo
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_TIME_ZONE as CONF_TIME_ZONE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

CONF_TIME_FORMAT: str
DEFAULT_NAME: str
DEFAULT_TIME_STR_FORMAT: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class WorldClockSensor(SensorEntity):
    _attr_icon: str
    _attr_name: Any
    _time_zone: Any
    _time_format: Any
    def __init__(self, time_zone: Union[tzinfo, None], name: str, time_format: str) -> None: ...
    _attr_native_value: Any
    async def async_update(self) -> None: ...