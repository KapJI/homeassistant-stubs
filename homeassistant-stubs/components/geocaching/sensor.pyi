from .const import DOMAIN as DOMAIN
from .coordinator import GeocachingDataUpdateCoordinator as GeocachingDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from geocachingapi.models import GeocachingStatus as GeocachingStatus
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass
class GeocachingRequiredKeysMixin:
    value_fn: Callable[[GeocachingStatus], str | int | None]
    def __init__(self, value_fn) -> None: ...

@dataclass
class GeocachingSensorEntityDescription(SensorEntityDescription, GeocachingRequiredKeysMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSORS: tuple[GeocachingSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class GeocachingSensor(CoordinatorEntity[GeocachingDataUpdateCoordinator], SensorEntity):
    entity_description: GeocachingSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GeocachingDataUpdateCoordinator, description: GeocachingSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> str | int | None: ...
