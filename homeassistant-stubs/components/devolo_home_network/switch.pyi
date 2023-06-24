from .const import DOMAIN as DOMAIN, SWITCH_GUEST_WIFI as SWITCH_GUEST_WIFI, SWITCH_LEDS as SWITCH_LEDS
from .entity import DevoloCoordinatorEntity as DevoloCoordinatorEntity
from collections.abc import Awaitable, Callable as Callable
from devolo_plc_api.device import Device as Device
from devolo_plc_api.device_api import WifiGuestAccessGet
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any, Generic, TypeVar

_DataT = TypeVar('_DataT', bound=WifiGuestAccessGet | bool)

class DevoloSwitchRequiredKeysMixin(Generic[_DataT]):
    is_on_func: Callable[[_DataT], bool]
    turn_on_func: Callable[[Device], Awaitable[bool]]
    turn_off_func: Callable[[Device], Awaitable[bool]]
    def __init__(self, is_on_func, turn_on_func, turn_off_func) -> None: ...

class DevoloSwitchEntityDescription(SwitchEntityDescription, DevoloSwitchRequiredKeysMixin[_DataT]):
    def __init__(self, is_on_func, turn_on_func, turn_off_func, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

SWITCH_TYPES: dict[str, DevoloSwitchEntityDescription[Any]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloSwitchEntity(DevoloCoordinatorEntity[_DataT], SwitchEntity):
    entity_description: DevoloSwitchEntityDescription[_DataT]
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator[_DataT], description: DevoloSwitchEntityDescription[_DataT], device: Device) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
