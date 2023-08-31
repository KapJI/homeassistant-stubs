from .const import DOMAIN as DOMAIN
from .coordinator import StarlinkData as StarlinkData, StarlinkUpdateCoordinator as StarlinkUpdateCoordinator
from .entity import StarlinkEntity as StarlinkEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class StarlinkSwitchEntityDescriptionMixin:
    value_fn: Callable[[StarlinkData], bool | None]
    turn_on_fn: Callable[[StarlinkUpdateCoordinator], Awaitable[None]]
    turn_off_fn: Callable[[StarlinkUpdateCoordinator], Awaitable[None]]
    def __init__(self, value_fn, turn_on_fn, turn_off_fn) -> None: ...

class StarlinkSwitchEntityDescription(SwitchEntityDescription, StarlinkSwitchEntityDescriptionMixin):
    def __init__(self, value_fn, turn_on_fn, turn_off_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class StarlinkSwitchEntity(StarlinkEntity, SwitchEntity):
    entity_description: StarlinkSwitchEntityDescription
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

SWITCHES: Incomplete
