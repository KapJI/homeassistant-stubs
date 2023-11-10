from . import CoordinatorDataT as CoordinatorDataT, NextDnsConnectionUpdateCoordinator as NextDnsConnectionUpdateCoordinator
from .const import ATTR_CONNECTION as ATTR_CONNECTION, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Generic

PARALLEL_UPDATES: int

@dataclass
class NextDnsBinarySensorRequiredKeysMixin(Generic[CoordinatorDataT]):
    state: Callable[[CoordinatorDataT, str], bool]
    def __init__(self, state) -> None: ...

@dataclass
class NextDnsBinarySensorEntityDescription(BinarySensorEntityDescription, NextDnsBinarySensorRequiredKeysMixin[CoordinatorDataT]):
    def __init__(self, state, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NextDnsBinarySensor(CoordinatorEntity[NextDnsConnectionUpdateCoordinator], BinarySensorEntity):
    _attr_has_entity_name: bool
    entity_description: NextDnsBinarySensorEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, coordinator: NextDnsConnectionUpdateCoordinator, description: NextDnsBinarySensorEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
