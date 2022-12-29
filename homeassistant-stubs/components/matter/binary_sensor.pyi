from .entity import MatterEntity as MatterEntity, MatterEntityDescriptionBaseClass as MatterEntityDescriptionBaseClass
from .helpers import get_matter as get_matter
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from matter_server.common.models import device_types

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterBinarySensor(MatterEntity, BinarySensorEntity):
    entity_description: MatterBinarySensorEntityDescription
    _attr_is_on: Incomplete
    def _update_from_device(self) -> None: ...

class MatterOccupancySensor(MatterBinarySensor):
    _attr_device_class: Incomplete
    _attr_is_on: Incomplete
    def _update_from_device(self) -> None: ...

class MatterBinarySensorEntityDescription(BinarySensorEntityDescription, MatterEntityDescriptionBaseClass):
    def __init__(self, entity_cls, subscribe_attributes, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

MatterSensorEntityDescriptionFactory: Incomplete
DEVICE_ENTITY: dict[type[device_types.DeviceType], Union[MatterEntityDescriptionBaseClass, list[MatterEntityDescriptionBaseClass]]]
