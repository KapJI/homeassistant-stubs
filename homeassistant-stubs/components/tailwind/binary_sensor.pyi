from .const import DOMAIN as DOMAIN
from .coordinator import TailwindDataUpdateCoordinator as TailwindDataUpdateCoordinator
from .entity import TailwindDoorEntity as TailwindDoorEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from gotailwind import TailwindDoor as TailwindDoor
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(kw_only=True, frozen=True)
class TailwindDoorBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[TailwindDoor], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, is_on_fn) -> None: ...

DESCRIPTIONS: tuple[TailwindDoorBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailwindDoorBinarySensorEntity(TailwindDoorEntity, BinarySensorEntity):
    entity_description: TailwindDoorBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
