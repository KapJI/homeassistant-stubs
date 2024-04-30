from .const import DOMAIN as DOMAIN
from .coordinator import AsekoDataUpdateCoordinator as AsekoDataUpdateCoordinator
from .entity import AsekoEntity as AsekoEntity
from _typeshed import Incomplete
from aioaseko import Unit as Unit
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class AsekoBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Unit], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value_fn) -> None: ...

UNIT_BINARY_SENSORS: tuple[AsekoBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AsekoUnitBinarySensorEntity(AsekoEntity, BinarySensorEntity):
    entity_description: AsekoBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, unit: Unit, coordinator: AsekoDataUpdateCoordinator, entity_description: AsekoBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
