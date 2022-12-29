from . import BMWBaseEntity as BMWBaseEntity
from .const import DOMAIN as DOMAIN
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import MyBMWVehicle as MyBMWVehicle
from bimmer_connected.vehicle.remote_services import RemoteServiceStatus as RemoteServiceStatus
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

class BMWButtonEntityDescription(ButtonEntityDescription):
    enabled_when_read_only: bool
    remote_function: Union[Callable[[MyBMWVehicle], Coroutine[Any, Any, RemoteServiceStatus]], None]
    account_function: Union[Callable[[BMWDataUpdateCoordinator], Coroutine], None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, enabled_when_read_only, remote_function, account_function) -> None: ...

BUTTON_TYPES: tuple[BMWButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWButton(BMWBaseEntity, ButtonEntity):
    entity_description: BMWButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: MyBMWVehicle, description: BMWButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
