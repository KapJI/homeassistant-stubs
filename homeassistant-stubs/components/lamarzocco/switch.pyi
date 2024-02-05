from .const import DOMAIN as DOMAIN
from .coordinator import LaMarzoccoUpdateCoordinator as LaMarzoccoUpdateCoordinator
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoSwitchEntityDescription(LaMarzoccoEntityDescription, SwitchEntityDescription):
    control_fn: Callable[[LaMarzoccoUpdateCoordinator, bool], Coroutine[Any, Any, bool]]
    is_on_fn: Callable[[LaMarzoccoUpdateCoordinator], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, available_fn, supported_fn, control_fn, is_on_fn) -> None: ...

ENTITIES: tuple[LaMarzoccoSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoSwitchEntity(LaMarzoccoEntity, SwitchEntity):
    entity_description: LaMarzoccoSwitchEntityDescription
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
