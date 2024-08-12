from . import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lmcloud.lm_machine import LaMarzoccoMachine as LaMarzoccoMachine
from lmcloud.models import LaMarzoccoMachineConfig as LaMarzoccoMachineConfig
from typing import Any

STEAM_LEVEL_HA_TO_LM: Incomplete
STEAM_LEVEL_LM_TO_HA: Incomplete
PREBREW_MODE_HA_TO_LM: Incomplete
PREBREW_MODE_LM_TO_HA: Incomplete

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoSelectEntityDescription(LaMarzoccoEntityDescription, SelectEntityDescription):
    current_option_fn: Callable[[LaMarzoccoMachineConfig], str]
    select_option_fn: Callable[[LaMarzoccoMachine, str], Coroutine[Any, Any, bool]]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., options=..., available_fn=..., supported_fn=..., current_option_fn, select_option_fn) -> None: ...

ENTITIES: tuple[LaMarzoccoSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoSelectEntity(LaMarzoccoEntity, SelectEntity):
    entity_description: LaMarzoccoSelectEntityDescription
    @property
    def current_option(self) -> str: ...
    async def async_select_option(self, option: str) -> None: ...
