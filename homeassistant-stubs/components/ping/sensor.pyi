from . import PingConfigEntry as PingConfigEntry
from .coordinator import PingResult as PingResult, PingUpdateCoordinator as PingUpdateCoordinator
from .entity import PingEntity as PingEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class PingSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PingResult], float | None]
    has_fn: Callable[[PingResult], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn, has_fn) -> None: ...

SENSORS: tuple[PingSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PingSensor(PingEntity, SensorEntity):
    entity_description: PingSensorEntityDescription
    def __init__(self, config_entry: ConfigEntry, description: PingSensorEntityDescription, coordinator: PingUpdateCoordinator) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> float | None: ...
