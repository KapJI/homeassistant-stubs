from . import PingDomainData as PingDomainData
from .const import DOMAIN as DOMAIN
from .helpers import PingDataICMPLib as PingDataICMPLib, PingDataSubProcess as PingDataSubProcess
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
ATTR_ROUND_TRIP_TIME_AVG: str
ATTR_ROUND_TRIP_TIME_MAX: str
ATTR_ROUND_TRIP_TIME_MDEV: str
ATTR_ROUND_TRIP_TIME_MIN: str
CONF_PING_COUNT: str
DEFAULT_NAME: str
DEFAULT_PING_COUNT: int
SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class PingBinarySensor(RestoreEntity, BinarySensorEntity):
    _attr_device_class: Incomplete
    _attr_available: bool
    _attr_name: Incomplete
    _ping: Incomplete
    def __init__(self, name: str, ping: PingDataSubProcess | PingDataICMPLib) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    async def async_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
