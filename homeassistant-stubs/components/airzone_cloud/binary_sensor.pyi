import abc
from .const import DOMAIN as DOMAIN
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneEntity as AirzoneEntity, AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

class AirzoneBinarySensorEntityDescription(BinarySensorEntityDescription):
    attributes: dict[str, str] | None
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, attributes) -> None: ...

ZONE_BINARY_SENSOR_TYPES: Final[tuple[AirzoneBinarySensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneBinarySensor(AirzoneEntity, BinarySensorEntity, metaclass=abc.ABCMeta):
    entity_description: AirzoneBinarySensorEntityDescription
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_on: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _async_update_attrs(self) -> None: ...

class AirzoneZoneBinarySensor(AirzoneZoneEntity, AirzoneBinarySensor):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: AirzoneBinarySensorEntityDescription, zone_id: str, zone_data: dict[str, Any]) -> None: ...
