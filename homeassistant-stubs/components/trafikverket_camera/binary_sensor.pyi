from .const import DOMAIN as DOMAIN
from .coordinator import CameraData as CameraData, TVDataUpdateCoordinator as TVDataUpdateCoordinator
from .entity import TrafikverketCameraNonCameraEntity as TrafikverketCameraNonCameraEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

@dataclass
class DeviceBaseEntityDescriptionMixin:
    value_fn: Callable[[CameraData], bool | None]
    def __init__(self, value_fn) -> None: ...

@dataclass
class TVCameraSensorEntityDescription(BinarySensorEntityDescription, DeviceBaseEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BINARY_SENSOR_TYPE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TrafikverketCameraBinarySensor(TrafikverketCameraNonCameraEntity, BinarySensorEntity):
    entity_description: TVCameraSensorEntityDescription
    _attr_is_on: Incomplete
    def _update_attr(self) -> None: ...
