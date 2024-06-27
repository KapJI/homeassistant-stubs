from . import AutomowerConfigEntry as AutomowerConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerAvailableEntity as AutomowerAvailableEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from datetime import timedelta
from homeassistant.components.lawn_mower import LawnMowerActivity as LawnMowerActivity, LawnMowerEntity as LawnMowerEntity, LawnMowerEntityFeature as LawnMowerEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

DOCKED_ACTIVITIES: Incomplete
MOWING_ACTIVITIES: Incomplete
PAUSED_STATES: Incomplete
SUPPORT_STATE_SERVICES: Incomplete
MOW: str
PARK: str
OVERRIDE_MODES: Incomplete
_LOGGER: Incomplete

def handle_sending_exception(func: Callable[..., Awaitable[Any]]) -> Callable[..., Coroutine[Any, Any, None]]: ...
async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerLawnMowerEntity(AutomowerAvailableEntity, LawnMowerEntity):
    _attr_name: Incomplete
    _attr_supported_features = SUPPORT_STATE_SERVICES
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def activity(self) -> LawnMowerActivity: ...
    async def async_start_mowing(self) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_dock(self) -> None: ...
    async def async_override_schedule(self, override_mode: str, duration: timedelta) -> None: ...
