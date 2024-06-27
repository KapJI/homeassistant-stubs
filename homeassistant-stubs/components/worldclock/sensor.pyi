from _typeshed import Incomplete
from datetime import tzinfo
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_TIME_ZONE as CONF_TIME_ZONE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

CONF_TIME_FORMAT: str
DEFAULT_NAME: str
DEFAULT_TIME_STR_FORMAT: str
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class WorldClockSensor(SensorEntity):
    _attr_icon: str
    _attr_name: Incomplete
    _time_zone: Incomplete
    _time_format: Incomplete
    def __init__(self, time_zone: tzinfo | None, name: str, time_format: str) -> None: ...
    _attr_native_value: Incomplete
    async def async_update(self) -> None: ...
