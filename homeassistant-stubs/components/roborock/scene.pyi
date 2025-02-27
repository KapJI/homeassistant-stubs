from . import RoborockConfigEntry as RoborockConfigEntry
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockEntity as RoborockEntity
from _typeshed import Incomplete
from homeassistant.components.scene import Scene as SceneEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockSceneEntity(RoborockEntity, SceneEntity):
    entity_description: EntityDescription
    _scene_id: Incomplete
    _coordinator: Incomplete
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, entity_description: EntityDescription) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
