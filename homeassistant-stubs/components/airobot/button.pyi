from .const import DOMAIN as DOMAIN
from .coordinator import AirobotConfigEntry as AirobotConfigEntry, AirobotDataUpdateCoordinator as AirobotDataUpdateCoordinator
from .entity import AirobotEntity as AirobotEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AirobotButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[AirobotDataUpdateCoordinator], Coroutine[Any, Any, None]]

BUTTON_TYPES: tuple[AirobotButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AirobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirobotButton(AirobotEntity, ButtonEntity):
    entity_description: AirobotButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirobotDataUpdateCoordinator, description: AirobotButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
