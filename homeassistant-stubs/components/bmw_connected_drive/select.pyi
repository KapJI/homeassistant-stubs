from . import BMWBaseEntity as BMWBaseEntity
from .const import DOMAIN as DOMAIN
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfElectricCurrent as UnitOfElectricCurrent
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

@dataclass
class BMWRequiredKeysMixin:
    current_option: Callable[[MyBMWVehicle], str]
    remote_service: Callable[[MyBMWVehicle, str], Coroutine[Any, Any, Any]]
    def __init__(self, current_option, remote_service) -> None: ...

@dataclass
class BMWSelectEntityDescription(SelectEntityDescription, BMWRequiredKeysMixin):
    is_available: Callable[[MyBMWVehicle], bool] = ...
    dynamic_options: Callable[[MyBMWVehicle], list[str]] | None = ...
    def __init__(self, current_option, remote_service, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, options, is_available, dynamic_options) -> None: ...

SELECT_TYPES: dict[str, BMWSelectEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWSelect(BMWBaseEntity, SelectEntity):
    entity_description: BMWSelectEntityDescription
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    _attr_current_option: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWSelectEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
