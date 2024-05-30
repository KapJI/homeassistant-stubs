from . import PiHoleConfigEntry as PiHoleConfigEntry, PiHoleEntity as PiHoleEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from hole import Hole as Hole
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

@dataclass(frozen=True, kw_only=True)
class PiHoleBinarySensorEntityDescription(BinarySensorEntityDescription):
    state_value: Callable[[Hole], bool]
    extra_value: Callable[[Hole], dict[str, Any] | None] = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, state_value, extra_value) -> None: ...

BINARY_SENSOR_TYPES: tuple[PiHoleBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PiHoleConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PiHoleBinarySensor(PiHoleEntity, BinarySensorEntity):
    entity_description: PiHoleBinarySensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    def __init__(self, api: Hole, coordinator: DataUpdateCoordinator[None], name: str, server_unique_id: str, description: PiHoleBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
