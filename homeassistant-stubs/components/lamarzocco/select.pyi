from .const import DOMAIN as DOMAIN
from .coordinator import LaMarzoccoUpdateCoordinator as LaMarzoccoUpdateCoordinator
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lmcloud import LMCloud as LaMarzoccoClient
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoSelectEntityDescription(LaMarzoccoEntityDescription, SelectEntityDescription):
    current_option_fn: Callable[[LaMarzoccoClient], str]
    select_option_fn: Callable[[LaMarzoccoUpdateCoordinator, str], Coroutine[Any, Any, bool]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, options, available_fn, supported_fn, current_option_fn, select_option_fn) -> None: ...

ENTITIES: tuple[LaMarzoccoSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoSelectEntity(LaMarzoccoEntity, SelectEntity):
    entity_description: LaMarzoccoSelectEntityDescription
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
