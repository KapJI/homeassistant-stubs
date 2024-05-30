from . import TedeeConfigEntry as TedeeConfigEntry
from .entity import TedeeDescriptionEntity as TedeeDescriptionEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytedee_async import TedeeLock as TedeeLock

@dataclass(frozen=True, kw_only=True)
class TedeeBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[TedeeLock], bool | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, is_on_fn) -> None: ...

ENTITIES: tuple[TedeeBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TedeeConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TedeeBinarySensorEntity(TedeeDescriptionEntity, BinarySensorEntity):
    entity_description: TedeeBinarySensorEntityDescription
    @property
    def is_on(self) -> bool | None: ...
