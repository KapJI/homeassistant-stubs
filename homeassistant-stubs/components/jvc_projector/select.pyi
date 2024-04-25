from . import JvcProjectorDataUpdateCoordinator as JvcProjectorDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from .entity import JvcProjectorEntity as JvcProjectorEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from jvcprojector import JvcProjector as JvcProjector
from typing import Final

@dataclass(frozen=True, kw_only=True)
class JvcProjectorSelectDescription(SelectEntityDescription):
    command: Callable[[JvcProjector, str], Awaitable[None]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, options, command) -> None: ...

OPTIONS: Final[dict[str, dict[str, str]]]
SELECTS: Final[list[JvcProjectorSelectDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class JvcProjectorSelectEntity(JvcProjectorEntity, SelectEntity):
    entity_description: JvcProjectorSelectDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: JvcProjectorDataUpdateCoordinator, description: JvcProjectorSelectDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
