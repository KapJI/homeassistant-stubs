from .common import TCP_PLATFORM_SCHEMA as TCP_PLATFORM_SCHEMA, TcpEntity as TcpEntity
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from typing import Any, Final

PLATFORM_SCHEMA: Final[Any]

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: Union[dict[str, Any], None] = ...) -> None: ...

class TcpSensor(TcpEntity, SensorEntity):
    @property
    def state(self) -> StateType: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
