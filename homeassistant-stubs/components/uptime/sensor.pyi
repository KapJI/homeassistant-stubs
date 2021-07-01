from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DEFAULT_NAME: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class UptimeSensor(SensorEntity):
    _name: Any
    _state: Any
    def __init__(self, name: str) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def device_class(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def should_poll(self) -> bool: ...
