from .const import DOMAIN as DOMAIN
from .coordinator import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry, LaMarzoccoUpdateCoordinator as LaMarzoccoUpdateCoordinator
from .entity import LaMarzoccoBaseEntity as LaMarzoccoBaseEntity, LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pylamarzocco import LaMarzoccoMachine as LaMarzoccoMachine
from pylamarzocco.models import WakeUpScheduleSettings as WakeUpScheduleSettings
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoSwitchEntityDescription(LaMarzoccoEntityDescription, SwitchEntityDescription):
    control_fn: Callable[[LaMarzoccoMachine, bool], Coroutine[Any, Any, bool]]
    is_on_fn: Callable[[LaMarzoccoMachine], bool]

ENTITIES: tuple[LaMarzoccoSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LaMarzoccoSwitchEntity(LaMarzoccoEntity, SwitchEntity):
    entity_description: LaMarzoccoSwitchEntityDescription
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...

class LaMarzoccoAutoOnOffSwitchEntity(LaMarzoccoBaseEntity, SwitchEntity):
    coordinator: LaMarzoccoUpdateCoordinator
    _attr_translation_key: str
    _schedule_entry: Incomplete
    _identifier: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_entity_category: Incomplete
    def __init__(self, coordinator: LaMarzoccoUpdateCoordinator, schedule_entry: WakeUpScheduleSettings) -> None: ...
    async def _async_enable(self, state: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
