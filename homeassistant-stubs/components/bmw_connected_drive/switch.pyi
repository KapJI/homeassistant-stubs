from . import BMWBaseEntity as BMWBaseEntity
from .const import DOMAIN as DOMAIN
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

class BMWRequiredKeysMixin:
    value_fn: Callable[[MyBMWVehicle], bool]
    remote_service_on: Callable[[MyBMWVehicle], Coroutine[Any, Any, Any]]
    remote_service_off: Callable[[MyBMWVehicle], Coroutine[Any, Any, Any]]
    def __init__(self, value_fn, remote_service_on, remote_service_off) -> None: ...

class BMWSwitchEntityDescription(SwitchEntityDescription, BMWRequiredKeysMixin):
    is_available: Callable[[MyBMWVehicle], bool]
    dynamic_options: Callable[[MyBMWVehicle], list[str]] | None
    def __init__(self, value_fn, remote_service_on, remote_service_off, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, is_available, dynamic_options) -> None: ...

CHARGING_STATE_ON: Incomplete
NUMBER_TYPES: list[BMWSwitchEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWSwitch(BMWBaseEntity, SwitchEntity):
    entity_description: BMWSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
