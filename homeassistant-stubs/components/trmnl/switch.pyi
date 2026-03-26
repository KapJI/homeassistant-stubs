from . import TRMNLConfigEntry as TRMNLConfigEntry
from .coordinator import TRMNLCoordinator as TRMNLCoordinator
from .entity import TRMNLEntity as TRMNLEntity, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from trmnl.models import Device as Device
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TRMNLSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[Device], bool]
    set_value_fn: Callable[[TRMNLCoordinator, int, bool], Coroutine[Any, Any, None]]

SWITCH_DESCRIPTIONS: tuple[TRMNLSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TRMNLConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TRMNLSwitchEntity(TRMNLEntity, SwitchEntity):
    entity_description: TRMNLSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: TRMNLCoordinator, device_id: int, description: TRMNLSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
