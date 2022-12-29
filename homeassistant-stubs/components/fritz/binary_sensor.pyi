from .common import AvmWrapper as AvmWrapper, ConnectionInfo as ConnectionInfo, FritzBoxBaseEntity as FritzBoxBaseEntity
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete

class FritzBinarySensorEntityDescription(BinarySensorEntityDescription):
    is_suitable: Callable[[ConnectionInfo], bool]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, is_suitable) -> None: ...

SENSOR_TYPES: tuple[FritzBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxBinarySensor(FritzBoxBaseEntity, BinarySensorEntity):
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str, description: BinarySensorEntityDescription) -> None: ...
    _attr_is_on: Incomplete
    _attr_extra_state_attributes: Incomplete
    def update(self) -> None: ...
