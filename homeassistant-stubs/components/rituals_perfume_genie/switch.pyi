from .const import DOMAIN as DOMAIN
from .coordinator import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .entity import DiffuserEntity as DiffuserEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser
from typing import Any

@dataclass
class RitualsEntityDescriptionMixin:
    is_on_fn: Callable[[Diffuser], bool]
    turn_on_fn: Callable[[Diffuser], Awaitable[None]]
    turn_off_fn: Callable[[Diffuser], Awaitable[None]]
    def __init__(self, is_on_fn, turn_on_fn, turn_off_fn) -> None: ...

@dataclass
class RitualsSwitchEntityDescription(SwitchEntityDescription, RitualsEntityDescriptionMixin):
    def __init__(self, is_on_fn, turn_on_fn, turn_off_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RitualsSwitchEntity(DiffuserEntity, SwitchEntity):
    entity_description: RitualsSwitchEntityDescription
    _attr_is_on: Incomplete
    def __init__(self, coordinator: RitualsDataUpdateCoordinator, description: RitualsSwitchEntityDescription) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
