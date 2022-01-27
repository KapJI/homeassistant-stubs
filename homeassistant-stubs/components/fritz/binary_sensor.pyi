from .common import AvmWrapper as AvmWrapper, FritzBoxBaseEntity as FritzBoxBaseEntity
from .const import DOMAIN as DOMAIN, MeshRoles as MeshRoles
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any

class FritzBinarySensorEntityDescription(BinarySensorEntityDescription):
    exclude_mesh_role: MeshRoles
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, exclude_mesh_role) -> None: ...

SENSOR_TYPES: tuple[FritzBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxBinarySensor(FritzBoxBaseEntity, BinarySensorEntity):
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str, description: BinarySensorEntityDescription) -> None: ...
    _attr_is_on: Any
    _attr_extra_state_attributes: Any
    def update(self) -> None: ...
