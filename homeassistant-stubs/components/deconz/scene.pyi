from . import DeconzConfigEntry as DeconzConfigEntry
from .entity import DeconzSceneMixin as DeconzSceneMixin
from homeassistant.components.scene import DOMAIN as SCENE_DOMAIN, Scene as Scene
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pydeconz.models.event import EventType as EventType
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: DeconzConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DeconzScene(DeconzSceneMixin, Scene):
    TYPE = SCENE_DOMAIN
    async def async_activate(self, **kwargs: Any) -> None: ...
