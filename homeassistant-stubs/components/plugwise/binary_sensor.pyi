from .const import DOMAIN as DOMAIN
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from plugwise.constants import BinarySensorType as BinarySensorType
from typing import Any

SEVERITIES: Incomplete

@dataclass
class PlugwiseBinarySensorEntityDescription(BinarySensorEntityDescription):
    key: BinarySensorType
    icon_off: str | None = ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, icon_off) -> None: ...

BINARY_SENSORS: tuple[PlugwiseBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PlugwiseBinarySensorEntity(PlugwiseEntity, BinarySensorEntity):
    entity_description: PlugwiseBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str, description: PlugwiseBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
