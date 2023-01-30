from . import PiHoleEntity as PiHoleEntity
from .const import DATA_KEY_API as DATA_KEY_API, DATA_KEY_COORDINATOR as DATA_KEY_COORDINATOR
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from hole import Hole as Hole
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class RequiredPiHoleBinaryDescription:
    state_value: Callable[[Hole], bool]
    def __init__(self, state_value) -> None: ...

class PiHoleBinarySensorEntityDescription(BinarySensorEntityDescription, RequiredPiHoleBinaryDescription):
    extra_value: Callable[[Hole], Union[dict[str, Any], None]]
    def __init__(self, state_value, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, extra_value) -> None: ...

BINARY_SENSOR_TYPES: tuple[PiHoleBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PiHoleBinarySensor(PiHoleEntity, BinarySensorEntity):
    entity_description: PiHoleBinarySensorEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, api: Hole, coordinator: DataUpdateCoordinator, name: str, server_unique_id: str, description: PiHoleBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
