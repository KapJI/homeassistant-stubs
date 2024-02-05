from .const import DOMAIN as DOMAIN
from .coordinator import TechnoVEDataUpdateCoordinator as TechnoVEDataUpdateCoordinator
from .entity import TechnoVEEntity as TechnoVEEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from technove import Station as TechnoVEStation

@dataclass(frozen=True, kw_only=True)
class TechnoVEBinarySensorDescription(BinarySensorEntityDescription):
    value_fn: Callable[[TechnoVEStation], bool | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_fn) -> None: ...

BINARY_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TechnoVEBinarySensorEntity(TechnoVEEntity, BinarySensorEntity):
    entity_description: TechnoVEBinarySensorDescription
    def __init__(self, coordinator: TechnoVEDataUpdateCoordinator, description: TechnoVEBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
