from . import QubeConfigEntry as QubeConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import QubeCoordinator as QubeCoordinator
from .entity import QubeEntity as QubeEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class QubeSwitchEntityDescription(SwitchEntityDescription):
    register_key: str

SWITCH_TYPES: tuple[QubeSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: QubeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class QubeSwitch(QubeEntity, SwitchEntity):
    entity_description: QubeSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: QubeCoordinator, entry: QubeConfigEntry, description: QubeSwitchEntityDescription) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    async def _async_write_switch(self, value: bool) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
