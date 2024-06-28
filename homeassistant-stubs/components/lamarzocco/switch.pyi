from . import LaMarzoccoConfigEntry as LaMarzoccoConfigEntry
from .coordinator import LaMarzoccoUpdateCoordinator as LaMarzoccoUpdateCoordinator
from .entity import LaMarzoccoBaseEntity as LaMarzoccoBaseEntity, LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lmcloud.lm_machine import LaMarzoccoMachine as LaMarzoccoMachine
from lmcloud.models import LaMarzoccoMachineConfig as LaMarzoccoMachineConfig
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoSwitchEntityDescription(LaMarzoccoEntityDescription, SwitchEntityDescription):
    control_fn: Callable[[LaMarzoccoMachine, bool], Coroutine[Any, Any, bool]]
    is_on_fn: Callable[[LaMarzoccoMachineConfig], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, available_fn, supported_fn, control_fn, is_on_fn) -> None: ...

ENTITIES: tuple[LaMarzoccoSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LaMarzoccoConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoSwitchEntity(LaMarzoccoEntity, SwitchEntity):
    entity_description: LaMarzoccoSwitchEntityDescription
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...

class LaMarzoccoAutoOnOffSwitchEntity(LaMarzoccoBaseEntity, SwitchEntity):
    coordinator: LaMarzoccoUpdateCoordinator
    _attr_translation_key: str
    _identifier: Incomplete
    _attr_translation_placeholders: Incomplete
    entity_category: Incomplete
    def __init__(self, coordinator: LaMarzoccoUpdateCoordinator, identifier: str) -> None: ...
    async def _async_enable(self, state: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
