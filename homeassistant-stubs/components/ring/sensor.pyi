from . import RingData as RingData
from .const import DOMAIN as DOMAIN
from .coordinator import RingDataCoordinator as RingDataCoordinator
from .entity import RingDeviceT as RingDeviceT, RingEntity as RingEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from ring_doorbell import RingEventKind, RingGeneric
from typing import Any, Generic

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingSensor(RingEntity[RingDeviceT], SensorEntity):
    entity_description: RingSensorEntityDescription[RingDeviceT]
    _attr_unique_id: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, device: RingDeviceT, coordinator: RingDataCoordinator, description: RingSensorEntityDescription[RingDeviceT]) -> None: ...
    _device: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _handle_coordinator_update(self) -> None: ...

def _get_last_event(history_data: list[dict[str, Any]], kind: RingEventKind | None) -> dict[str, Any] | None: ...
def _get_last_event_attrs(history_data: list[dict[str, Any]], kind: RingEventKind | None) -> dict[str, Any] | None: ...

@dataclass(frozen=True, kw_only=True)
class RingSensorEntityDescription(SensorEntityDescription, Generic[RingDeviceT]):
    value_fn: Callable[[RingDeviceT], StateType] = ...
    exists_fn: Callable[[RingGeneric], bool] = ...
    extra_state_attributes_fn: Callable[[RingDeviceT], dict[str, Any] | None] = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn, exists_fn, extra_state_attributes_fn) -> None: ...

SENSOR_TYPES: tuple[RingSensorEntityDescription[Any], ...]
