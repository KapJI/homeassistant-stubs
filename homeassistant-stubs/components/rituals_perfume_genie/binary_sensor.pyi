from .const import DOMAIN as DOMAIN
from .coordinator import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .entity import DiffuserEntity as DiffuserEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser

class RitualsentityDescriptionMixin:
    is_on_fn: Callable[[Diffuser], bool]
    has_fn: Callable[[Diffuser], bool]
    def __init__(self, is_on_fn, has_fn) -> None: ...

class RitualsBinarySensorEntityDescription(BinarySensorEntityDescription, RitualsentityDescriptionMixin):
    def __init__(self, is_on_fn, has_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RitualsBinarySensorEntity(DiffuserEntity, BinarySensorEntity):
    entity_description: RitualsBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
