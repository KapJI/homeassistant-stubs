from .const import CONF_LINE as CONF_LINE, DOMAIN as DOMAIN, TUBE_LINES as TUBE_LINES
from .coordinator import LondonTubeCoordinator as LondonTubeCoordinator, LondonUndergroundConfigEntry as LondonUndergroundConfigEntry
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: LondonUndergroundConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LondonTubeSensor(CoordinatorEntity[LondonTubeCoordinator], SensorEntity):
    _attr_attribution: str
    _attr_icon: str
    _attr_has_entity_name: bool
    _name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: LondonTubeCoordinator, name: str) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
