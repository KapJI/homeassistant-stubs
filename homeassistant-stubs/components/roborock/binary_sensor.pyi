from . import RoborockCoordinators as RoborockCoordinators
from .const import DOMAIN as DOMAIN
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .device import RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from roborock.roborock_typing import DeviceProp as DeviceProp

@dataclass(frozen=True, kw_only=True)
class RoborockBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[DeviceProp], bool | int | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_fn) -> None: ...

BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockBinarySensorEntity(RoborockCoordinatedEntityV1, BinarySensorEntity):
    entity_description: RoborockBinarySensorDescription
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, description: RoborockBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
