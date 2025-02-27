from .coordinator import LetPotConfigEntry as LetPotConfigEntry, LetPotDeviceCoordinator as LetPotDeviceCoordinator
from .entity import LetPotEntity as LetPotEntity, LetPotEntityDescription as LetPotEntityDescription, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from letpot.deviceclient import LetPotDeviceClient as LetPotDeviceClient
from letpot.models import LetPotDeviceStatus as LetPotDeviceStatus
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LetPotSwitchEntityDescription(LetPotEntityDescription, SwitchEntityDescription):
    value_fn: Callable[[LetPotDeviceStatus], bool | None]
    set_value_fn: Callable[[LetPotDeviceClient, bool], Coroutine[Any, Any, None]]

SWITCHES: tuple[LetPotSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: LetPotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LetPotSwitchEntity(LetPotEntity, SwitchEntity):
    entity_description: LetPotSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LetPotDeviceCoordinator, description: LetPotSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    @exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
