from . import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lmcloud.lm_machine import LaMarzoccoMachine as LaMarzoccoMachine
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoButtonEntityDescription(LaMarzoccoEntityDescription, ButtonEntityDescription):
    press_fn: Callable[[LaMarzoccoMachine], Coroutine[Any, Any, None]]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., available_fn=..., supported_fn=..., press_fn) -> None: ...

ENTITIES: tuple[LaMarzoccoButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoButtonEntity(LaMarzoccoEntity, ButtonEntity):
    entity_description: LaMarzoccoButtonEntityDescription
    async def async_press(self) -> None: ...
