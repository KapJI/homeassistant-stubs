from . import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity, ElkM1ConfigEntry as ElkM1ConfigEntry, create_elk_entities as create_elk_entities
from elkm1_lib.outputs import Output as Output
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElkOutput(ElkAttachedEntity, SwitchEntity):
    _element: Output
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
