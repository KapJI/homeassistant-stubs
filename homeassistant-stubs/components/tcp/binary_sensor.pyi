from .common import TCP_PLATFORM_SCHEMA as TCP_PLATFORM_SCHEMA, TcpEntity as TcpEntity
from .const import CONF_VALUE_ON as CONF_VALUE_ON
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final

PLATFORM_SCHEMA: Final[Any]

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: Union[dict[str, Any], None] = ...) -> None: ...

class TcpBinarySensor(TcpEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...
