import abc
from . import SurePetcareDataCoordinator as SurePetcareDataCoordinator
from .const import DOMAIN as DOMAIN
from .entity import SurePetcareEntity as SurePetcareEntity
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from surepy.entities import SurepyEntity as SurepyEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SurePetcareBinarySensor(SurePetcareEntity, BinarySensorEntity, metaclass=abc.ABCMeta):
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, surepetcare_id: int, coordinator: SurePetcareDataCoordinator) -> None: ...

class Hub(SurePetcareBinarySensor):
    _attr_device_class: Any
    _attr_entity_category: Any
    @property
    def available(self) -> bool: ...
    _attr_is_on: Any
    _attr_extra_state_attributes: Any
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...

class Pet(SurePetcareBinarySensor):
    _attr_device_class: Any
    _attr_is_on: Any
    _attr_extra_state_attributes: Any
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...

class DeviceConnectivity(SurePetcareBinarySensor):
    _attr_device_class: Any
    _attr_entity_category: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, surepetcare_id: int, coordinator: SurePetcareDataCoordinator) -> None: ...
    _attr_is_on: Any
    _attr_extra_state_attributes: Any
    def _update_attr(self, surepy_entity: SurepyEntity) -> None: ...
