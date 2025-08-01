import abc
from . import HistoryStatsConfigEntry as HistoryStatsConfigEntry
from .const import CONF_DURATION as CONF_DURATION, CONF_END as CONF_END, CONF_PERIOD_KEYS as CONF_PERIOD_KEYS, CONF_START as CONF_START, CONF_TYPE_COUNT as CONF_TYPE_COUNT, CONF_TYPE_KEYS as CONF_TYPE_KEYS, CONF_TYPE_RATIO as CONF_TYPE_RATIO, CONF_TYPE_TIME as CONF_TYPE_TIME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import HistoryStatsUpdateCoordinator as HistoryStatsUpdateCoordinator
from .data import HistoryStats as HistoryStats
from .helpers import pretty_ratio as pretty_ratio
from _typeshed import Incomplete
from abc import abstractmethod
from collections.abc import Callable as Callable, Mapping
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_STATE as CONF_STATE, CONF_TYPE as CONF_TYPE, CONF_UNIQUE_ID as CONF_UNIQUE_ID, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.device import async_entity_id_to_device as async_entity_id_to_device
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.reload import async_setup_reload_service as async_setup_reload_service
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

UNITS: dict[str, str]
ICON: str

def exactly_two_period_keys[_T: dict[str, Any]](conf: _T) -> _T: ...

PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: HistoryStatsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HistoryStatsSensorBase(CoordinatorEntity[HistoryStatsUpdateCoordinator], SensorEntity, metaclass=abc.ABCMeta):
    _attr_icon = ICON
    _attr_name: Incomplete
    def __init__(self, coordinator: HistoryStatsUpdateCoordinator, name: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @callback
    @abstractmethod
    def _process_update(self) -> None: ...

class HistoryStatsSensor(HistoryStatsSensorBase):
    _attr_state_class: Incomplete
    _preview_callback: Callable[[Exception | None, str, Mapping[str, Any]], None] | None
    _attr_native_unit_of_measurement: Incomplete
    _type: Incomplete
    _attr_unique_id: Incomplete
    device_entry: Incomplete
    _attr_device_class: Incomplete
    _attr_suggested_display_precision: int
    def __init__(self, hass: HomeAssistant, *, coordinator: HistoryStatsUpdateCoordinator, sensor_type: str, name: str, unique_id: str | None, source_entity_id: str) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _process_update(self) -> None: ...
    async def async_start_preview(self, preview_callback: Callable[[Exception | None, str, Mapping[str, Any]], None]) -> CALLBACK_TYPE: ...
