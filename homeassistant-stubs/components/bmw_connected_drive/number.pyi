from . import BMWBaseEntity as BMWBaseEntity
from .const import DOMAIN as DOMAIN
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

class BMWRequiredKeysMixin:
    value_fn: Callable[[MyBMWVehicle], float | int | None]
    remote_service: Callable[[MyBMWVehicle, float | int], Coroutine[Any, Any, Any]]
    def __init__(self, value_fn, remote_service) -> None: ...

class BMWNumberEntityDescription(NumberEntityDescription, BMWRequiredKeysMixin):
    is_available: Callable[[MyBMWVehicle], bool]
    dynamic_options: Callable[[MyBMWVehicle], list[str]] | None
    def __init__(self, value_fn, remote_service, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, max_value, min_value, mode, native_max_value, native_min_value, native_step, native_unit_of_measurement, step, is_available, dynamic_options) -> None: ...

NUMBER_TYPES: list[BMWNumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWNumber(BMWBaseEntity, NumberEntity):
    entity_description: BMWNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWNumberEntityDescription) -> None: ...
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...
