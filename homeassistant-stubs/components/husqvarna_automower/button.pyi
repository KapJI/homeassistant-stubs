from . import AutomowerConfigEntry as AutomowerConfigEntry
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerAvailableEntity as AutomowerAvailableEntity, _check_error_free as _check_error_free, handle_sending_exception as handle_sending_exception
from _typeshed import Incomplete
from aioautomower.model import MowerAttributes as MowerAttributes
from aioautomower.session import AutomowerSession as AutomowerSession
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def _async_set_time(session: AutomowerSession, mower_id: str) -> None: ...

@dataclass(frozen=True, kw_only=True)
class AutomowerButtonEntityDescription(ButtonEntityDescription):
    available_fn: Callable[[MowerAttributes], bool] = ...
    exists_fn: Callable[[MowerAttributes], bool] = ...
    press_fn: Callable[[AutomowerSession, str], Awaitable[Any]]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., available_fn=..., exists_fn=..., press_fn) -> None: ...

BUTTON_TYPES: tuple[AutomowerButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerButtonEntity(AutomowerAvailableEntity, ButtonEntity):
    entity_description: AutomowerButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, description: AutomowerButtonEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_press(self) -> None: ...
