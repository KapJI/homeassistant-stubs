from . import AutomowerConfigEntry as AutomowerConfigEntry
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerControlEntity as AutomowerControlEntity, handle_sending_exception as handle_sending_exception
from _typeshed import Incomplete
from aioautomower.model import MowerAttributes as MowerAttributes
from aioautomower.session import AutomowerSession as AutomowerSession
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_reset_cutting_blade_usage_time(session: AutomowerSession, mower_id: str) -> None: ...
def reset_cutting_blade_usage_time_availability(data: MowerAttributes) -> bool: ...

@dataclass(frozen=True, kw_only=True)
class AutomowerButtonEntityDescription(ButtonEntityDescription):
    available_fn: Callable[[MowerAttributes], bool] = ...
    exists_fn: Callable[[MowerAttributes], bool] = ...
    press_fn: Callable[[AutomowerSession, str], Awaitable[Any]]
    poll_after_sending: bool = ...

MOWER_BUTTON_TYPES: tuple[AutomowerButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AutomowerButtonEntity(AutomowerControlEntity, ButtonEntity):
    entity_description: AutomowerButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, description: AutomowerButtonEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @handle_sending_exception
    async def async_press(self) -> None: ...
