from .const import DOMAIN as DOMAIN
from .coordinator import TechnoVEDataUpdateCoordinator as TechnoVEDataUpdateCoordinator
from .entity import TechnoVEEntity as TechnoVEEntity
from .helpers import technove_exception_handler as technove_exception_handler
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from technove import Station as TechnoVEStation, TechnoVE as TechnoVE
from typing import Any

@dataclass(frozen=True, kw_only=True)
class TechnoVESwitchDescription(SwitchEntityDescription):
    is_on_fn: Callable[[TechnoVEStation], bool]
    turn_on_fn: Callable[[TechnoVE], Awaitable[dict[str, Any]]]
    turn_off_fn: Callable[[TechnoVE], Awaitable[dict[str, Any]]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, is_on_fn, turn_on_fn, turn_off_fn) -> None: ...

SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TechnoVESwitchEntity(TechnoVEEntity, SwitchEntity):
    entity_description: TechnoVESwitchDescription
    def __init__(self, coordinator: TechnoVEDataUpdateCoordinator, description: TechnoVESwitchDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
