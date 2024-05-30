from . import TVCameraConfigEntry as TVCameraConfigEntry
from .coordinator import CameraData as CameraData
from .entity import TrafikverketCameraNonCameraEntity as TrafikverketCameraNonCameraEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TVCameraSensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[CameraData], bool | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_fn) -> None: ...

BINARY_SENSOR_TYPE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TVCameraConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TrafikverketCameraBinarySensor(TrafikverketCameraNonCameraEntity, BinarySensorEntity):
    entity_description: TVCameraSensorEntityDescription
    _attr_is_on: Incomplete
    def _update_attr(self) -> None: ...
