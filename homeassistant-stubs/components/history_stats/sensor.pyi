import abc
from . import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import HistoryStatsUpdateCoordinator as HistoryStatsUpdateCoordinator
from .data import HistoryStats as HistoryStats
from .helpers import pretty_ratio as pretty_ratio
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_STATE as CONF_STATE, CONF_TYPE as CONF_TYPE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

CONF_START: str
CONF_END: str
CONF_DURATION: str
CONF_PERIOD_KEYS: Incomplete
CONF_TYPE_TIME: str
CONF_TYPE_RATIO: str
CONF_TYPE_COUNT: str
CONF_TYPE_KEYS: Incomplete
DEFAULT_NAME: str
UNITS: dict[str, str]
ICON: str

def exactly_two_period_keys(conf: _T) -> _T: ...

PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class HistoryStatsSensorBase(CoordinatorEntity[HistoryStatsUpdateCoordinator], SensorEntity, metaclass=abc.ABCMeta):
    _attr_icon = ICON
    _attr_name: Incomplete
    def __init__(self, coordinator: HistoryStatsUpdateCoordinator, name: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @abstractmethod
    def _process_update(self) -> None: ...

class HistoryStatsSensor(HistoryStatsSensorBase):
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _type: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_class: Incomplete
    _attr_suggested_display_precision: int
    def __init__(self, coordinator: HistoryStatsUpdateCoordinator, sensor_type: str, name: str, unique_id: str | None) -> None: ...
    _attr_native_value: Incomplete
    def _process_update(self) -> None: ...
