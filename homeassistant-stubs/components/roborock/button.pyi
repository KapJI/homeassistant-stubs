from .coordinator import RoborockConfigEntry as RoborockConfigEntry, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockEntity as RoborockEntity, RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from roborock.roborock_typing import RoborockCommand
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockButtonDescription(ButtonEntityDescription):
    command: RoborockCommand
    param: list | dict | None

CONSUMABLE_BUTTON_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockButtonEntity(RoborockEntityV1, ButtonEntity):
    entity_description: RoborockButtonDescription
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockButtonDescription) -> None: ...
    async def async_press(self) -> None: ...

class RoborockRoutineButtonEntity(RoborockEntity, ButtonEntity):
    entity_description: ButtonEntityDescription
    _routine_id: Incomplete
    _coordinator: Incomplete
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, entity_description: ButtonEntityDescription) -> None: ...
    async def async_press(self, **kwargs: Any) -> None: ...
