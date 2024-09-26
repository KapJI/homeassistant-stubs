from . import RingConfigEntry as RingConfigEntry
from .coordinator import RingListenCoordinator as RingListenCoordinator
from .entity import DeprecatedInfo as DeprecatedInfo, RingBaseEntity as RingBaseEntity, RingDeviceT as RingDeviceT, RingEntityDescription as RingEntityDescription, async_check_create_deprecated as async_check_create_deprecated
from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_at as async_call_at
from ring_doorbell import RingCapability, RingEvent as RingEvent
from typing import Any, Generic

@dataclass(frozen=True, kw_only=True)
class RingBinarySensorEntityDescription(BinarySensorEntityDescription, RingEntityDescription, Generic[RingDeviceT]):
    capability: RingCapability
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., deprecated_info=..., capability) -> None: ...

BINARY_SENSOR_TYPES: tuple[RingBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: RingConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RingBinarySensor(RingBaseEntity[RingListenCoordinator, RingDeviceT], BinarySensorEntity):
    _active_alert: RingEvent | None
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_on: bool
    _cancel_callback: Incomplete
    def __init__(self, device: RingDeviceT, coordinator: RingListenCoordinator, description: RingBinarySensorEntityDescription[RingDeviceT]) -> None: ...
    def _async_handle_event(self, alert: RingEvent) -> None: ...
    def _async_cancel_event(self, _now: Any) -> None: ...
    def _get_coordinator_alert(self) -> RingEvent | None: ...
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
