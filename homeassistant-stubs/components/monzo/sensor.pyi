from . import MonzoCoordinator as MonzoCoordinator
from .const import DOMAIN as DOMAIN
from .coordinator import MonzoData as MonzoData
from .entity import MonzoBaseEntity as MonzoBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

@dataclass(frozen=True, kw_only=True)
class MonzoSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any]], StateType]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

ACCOUNT_SENSORS: Incomplete
POT_SENSORS: Incomplete
MODEL_POT: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MonzoSensor(MonzoBaseEntity, SensorEntity):
    entity_description: MonzoSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MonzoCoordinator, entity_description: MonzoSensorEntityDescription, index: int, device_model: str, data_accessor: Callable[[MonzoData], list[dict[str, Any]]]) -> None: ...
    @property
    def native_value(self) -> StateType: ...
