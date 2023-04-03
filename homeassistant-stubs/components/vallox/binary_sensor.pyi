from . import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator, ValloxEntity as ValloxEntity
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class ValloxBinarySensorEntity(ValloxEntity, BinarySensorEntity):
    entity_description: ValloxBinarySensorEntityDescription
    _attr_entity_category: Incomplete
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class ValloxMetricKeyMixin:
    metric_key: str
    def __init__(self, metric_key) -> None: ...

class ValloxBinarySensorEntityDescription(BinarySensorEntityDescription, ValloxMetricKeyMixin):
    def __init__(self, metric_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BINARY_SENSOR_ENTITIES: tuple[ValloxBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
