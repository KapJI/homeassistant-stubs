from . import FritzBoxDeviceEntity as FritzBoxDeviceEntity
from .const import CONF_COORDINATOR as CONF_COORDINATOR
from .coordinator import FritzboxDataUpdateCoordinator as FritzboxDataUpdateCoordinator
from .model import FritzEntityDescriptionMixinBase as FritzEntityDescriptionMixinBase
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyfritzhome.fritzhomedevice import FritzhomeDevice as FritzhomeDevice
from typing import Final

class FritzEntityDescriptionMixinBinarySensor(FritzEntityDescriptionMixinBase):
    is_on: Callable[[FritzhomeDevice], Union[bool, None]]
    def __init__(self, suitable, is_on) -> None: ...

class FritzBinarySensorEntityDescription(BinarySensorEntityDescription, FritzEntityDescriptionMixinBinarySensor):
    def __init__(self, suitable, is_on, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BINARY_SENSOR_TYPES: Final[tuple[FritzBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzboxBinarySensor(FritzBoxDeviceEntity, BinarySensorEntity):
    entity_description: FritzBinarySensorEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FritzboxDataUpdateCoordinator, ain: str, entity_description: FritzBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
