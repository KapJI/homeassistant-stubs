from .coordinator import AvmWrapper as AvmWrapper, FritzConfigEntry as FritzConfigEntry
from .entity import FritzBoxBaseCoordinatorEntity as FritzBoxBaseCoordinatorEntity, FritzEntityDescription as FritzEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class FritzUpdateEntityDescription(UpdateEntityDescription, FritzEntityDescription): ...

async def async_setup_entry(hass: HomeAssistant, entry: FritzConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FritzBoxUpdateEntity(FritzBoxBaseCoordinatorEntity, UpdateEntity):
    _attr_entity_category: Incomplete
    _attr_supported_features: Incomplete
    _attr_title: str
    entity_description: FritzUpdateEntityDescription
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    @property
    def release_url(self) -> str | None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
