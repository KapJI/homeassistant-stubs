from . import AnalyticsInsightsData as AnalyticsInsightsData
from .const import DOMAIN as DOMAIN
from .coordinator import AnalyticsData as AnalyticsData, HomeassistantAnalyticsDataUpdateCoordinator as HomeassistantAnalyticsDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class AnalyticsSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[AnalyticsData], StateType]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

def get_core_integration_entity_description(domain: str, name: str) -> AnalyticsSensorEntityDescription: ...
def get_custom_integration_entity_description(domain: str) -> AnalyticsSensorEntityDescription: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HomeassistantAnalyticsSensor(CoordinatorEntity[HomeassistantAnalyticsDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_entity_category: Incomplete
    entity_description: AnalyticsSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HomeassistantAnalyticsDataUpdateCoordinator, entity_description: AnalyticsSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
