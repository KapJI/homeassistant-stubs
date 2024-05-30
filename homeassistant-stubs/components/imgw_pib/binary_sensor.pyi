from . import ImgwPibConfigEntry as ImgwPibConfigEntry
from .coordinator import ImgwPibDataUpdateCoordinator as ImgwPibDataUpdateCoordinator
from .entity import ImgwPibEntity as ImgwPibEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from imgw_pib.model import HydrologicalData as HydrologicalData

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ImgwPibBinarySensorEntityDescription(BinarySensorEntityDescription):
    value: Callable[[HydrologicalData], bool | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, value) -> None: ...

BINARY_SENSOR_TYPES: tuple[ImgwPibBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ImgwPibConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ImgwPibBinarySensorEntity(ImgwPibEntity, BinarySensorEntity):
    entity_description: ImgwPibBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ImgwPibDataUpdateCoordinator, description: ImgwPibBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
