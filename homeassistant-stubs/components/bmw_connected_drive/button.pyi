from . import BMWBaseEntity as BMWBaseEntity
from .const import DOMAIN as DOMAIN
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from bimmer_connected.vehicle.remote_services import RemoteServiceStatus as RemoteServiceStatus
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

@dataclass
class BMWRequiredKeysMixin:
    remote_function: Callable[[MyBMWVehicle], Coroutine[Any, Any, RemoteServiceStatus]]
    def __init__(self, remote_function) -> None: ...

@dataclass
class BMWButtonEntityDescription(ButtonEntityDescription, BMWRequiredKeysMixin):
    enabled_when_read_only: bool = ...
    is_available: Callable[[MyBMWVehicle], bool] = ...
    def __init__(self, remote_function, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, enabled_when_read_only, is_available) -> None: ...

BUTTON_TYPES: tuple[BMWButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWButton(BMWBaseEntity, ButtonEntity):
    entity_description: BMWButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
