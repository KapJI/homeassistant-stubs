from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Any
CONF_HOSTNAME: str
CONF_IPV6: str
CONF_RESOLVER: str
CONF_RESOLVER_IPV6: str
DEFAULT_HOSTNAME: str
DEFAULT_IPV6: bool
DEFAULT_NAME: str
DEFAULT_RESOLVER: str
DEFAULT_RESOLVER_IPV6: str
SCAN_INTERVAL: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_devices: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class WanIpSensor(SensorEntity):
    _attr_name: Any
    hostname: Any
    resolver: Any
    querytype: Any
    def __init__(self, name: str, hostname: str, resolver: str, ipv6: bool) -> None: ...
    _attr_state: Any
    async def async_update(self) -> None: ...
