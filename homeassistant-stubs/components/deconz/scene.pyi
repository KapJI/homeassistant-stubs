from .deconz_device import DeconzSceneMixin as DeconzSceneMixin
from .gateway import get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from homeassistant.components.scene import DOMAIN as DOMAIN, Scene as Scene
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzScene(DeconzSceneMixin, Scene):
    TYPE: Incomplete
    async def async_activate(self, **kwargs: Any) -> None: ...
