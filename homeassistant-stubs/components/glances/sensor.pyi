from . import GlancesDataUpdateCoordinator as GlancesDataUpdateCoordinator
from .const import CPU_ICON as CPU_ICON, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, PERCENTAGE as PERCENTAGE, Platform as Platform, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, UnitOfInformation as UnitOfInformation, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass
class GlancesSensorEntityDescriptionMixin:
    type: str
    name_suffix: str
    def __init__(self, type, name_suffix) -> None: ...

@dataclass
class GlancesSensorEntityDescription(SensorEntityDescription, GlancesSensorEntityDescriptionMixin):
    def __init__(self, type, name_suffix, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GlancesSensor(CoordinatorEntity[GlancesDataUpdateCoordinator], SensorEntity):
    entity_description: GlancesSensorEntityDescription
    _attr_has_entity_name: bool
    _sensor_name_prefix: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: GlancesDataUpdateCoordinator, name: str | None, sensor_name_prefix: str, description: GlancesSensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
