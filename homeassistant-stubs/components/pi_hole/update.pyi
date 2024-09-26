from . import PiHoleConfigEntry as PiHoleConfigEntry
from .entity import PiHoleEntity as PiHoleEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from hole import Hole as Hole
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription
from homeassistant.const import CONF_NAME as CONF_NAME, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

@dataclass(frozen=True)
class PiHoleUpdateEntityDescription(UpdateEntityDescription):
    installed_version: Callable[[dict], str | None] = ...
    latest_version: Callable[[dict], str | None] = ...
    has_update: Callable[[dict], bool | None] = ...
    release_base_url: str | None = ...
    title: str | None = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., installed_version=..., latest_version=..., has_update=..., release_base_url=..., title=...) -> None: ...

UPDATE_ENTITY_TYPES: tuple[PiHoleUpdateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PiHoleConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PiHoleUpdateEntity(PiHoleEntity, UpdateEntity):
    entity_description: PiHoleUpdateEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_title: Incomplete
    def __init__(self, api: Hole, coordinator: DataUpdateCoordinator[None], name: str, server_unique_id: str, description: PiHoleUpdateEntityDescription) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    @property
    def release_url(self) -> str | None: ...
