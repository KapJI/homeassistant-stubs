from .const import CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_RESUME_SCHEDULE_KEY as CHARGER_RESUME_SCHEDULE_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY
from .coordinator import WallboxConfigEntry as WallboxConfigEntry, WallboxCoordinator as WallboxCoordinator
from .entity import WallboxEntity as WallboxEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

@dataclass(frozen=True, kw_only=True)
class WallboxButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[WallboxCoordinator], Awaitable[None]]

BUTTON_TYPES: dict[str, WallboxButtonEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: WallboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

PARALLEL_UPDATES: int

class WallboxButton(WallboxEntity, ButtonEntity):
    entity_description: WallboxButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WallboxCoordinator, description: WallboxButtonEntityDescription) -> None: ...
    @override
    async def async_press(self) -> None: ...
