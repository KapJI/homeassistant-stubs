from _typeshed import Incomplete
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_MODE as ATTR_MODE, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
ATTR_CLIMB: str
ATTR_ELEVATION: str
ATTR_GPS_TIME: str
ATTR_SPEED: str
DEFAULT_HOST: str
DEFAULT_NAME: str
DEFAULT_PORT: int

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class GpsdSensor(SensorEntity):
    hass: Incomplete
    _name: Incomplete
    _host: Incomplete
    _port: Incomplete
    agps_thread: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, host: str, port: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def icon(self) -> str: ...
