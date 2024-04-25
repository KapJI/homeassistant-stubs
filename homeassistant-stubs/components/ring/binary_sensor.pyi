from . import RingData as RingData
from .const import DOMAIN as DOMAIN
from .coordinator import RingNotificationsCoordinator as RingNotificationsCoordinator
from .entity import RingBaseEntity as RingBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from ring_doorbell import Ring as Ring, RingEvent as RingEvent, RingGeneric as RingGeneric
from typing import Any

@dataclass(frozen=True, kw_only=True)
class RingBinarySensorEntityDescription(BinarySensorEntityDescription):
    exists_fn: Callable[[RingGeneric], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, exists_fn) -> None: ...

BINARY_SENSOR_TYPES: tuple[RingBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingBinarySensor(RingBaseEntity[RingNotificationsCoordinator], BinarySensorEntity):
    _active_alert: RingEvent | None
    entity_description: RingBinarySensorEntityDescription
    _ring: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, ring: Ring, device: RingGeneric, coordinator: RingNotificationsCoordinator, description: RingBinarySensorEntityDescription) -> None: ...
    def _handle_coordinator_update(self, _: Any = None) -> None: ...
    def _update_alert(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
