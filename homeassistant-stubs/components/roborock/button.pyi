from .const import DOMAIN as DOMAIN
from .coordinator import RoborockB01Q10UpdateCoordinator as RoborockB01Q10UpdateCoordinator, RoborockConfigEntry as RoborockConfigEntry, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01, RoborockWashingMachineUpdateCoordinator as RoborockWashingMachineUpdateCoordinator
from .entity import RoborockCoordinatedEntityA01 as RoborockCoordinatedEntityA01, RoborockCoordinatedEntityB01Q10 as RoborockCoordinatedEntityB01Q10, RoborockEntity as RoborockEntity, RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from roborock.devices.traits.v1.consumeable import ConsumableAttribute
from roborock.roborock_message import RoborockZeoProtocol
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockButtonDescription(ButtonEntityDescription):
    attribute: ConsumableAttribute
    is_dock_entity: bool = ...
    is_supported: Callable[[RoborockDataUpdateCoordinator], bool] = ...

def _supports_dock_consumables(coordinator: RoborockDataUpdateCoordinator) -> bool: ...

CONSUMABLE_BUTTON_DESCRIPTIONS: Incomplete

@dataclass(frozen=True, kw_only=True)
class RoborockButtonDescriptionA01(ButtonEntityDescription):
    data_protocol: RoborockZeoProtocol

ZEO_BUTTON_DESCRIPTIONS: Incomplete
Q10_BUTTON_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockButtonEntity(RoborockEntityV1, ButtonEntity):
    entity_description: RoborockButtonDescription
    _consumable: Incomplete
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockButtonDescription) -> None: ...
    async def async_press(self) -> None: ...

class RoborockRoutineButtonEntity(RoborockEntity, ButtonEntity):
    entity_description: ButtonEntityDescription
    _routine_id: Incomplete
    _coordinator: Incomplete
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, entity_description: ButtonEntityDescription) -> None: ...
    async def async_press(self, **kwargs: Any) -> None: ...

class RoborockButtonEntityA01(RoborockCoordinatedEntityA01, ButtonEntity):
    entity_description: RoborockButtonDescriptionA01
    def __init__(self, coordinator: RoborockDataUpdateCoordinatorA01, entity_description: RoborockButtonDescriptionA01) -> None: ...
    async def async_press(self) -> None: ...

class RoborockQ10EmptyDustbinButtonEntity(RoborockCoordinatedEntityB01Q10, ButtonEntity):
    entity_description: ButtonEntityDescription
    coordinator: RoborockB01Q10UpdateCoordinator
    def __init__(self, coordinator: RoborockB01Q10UpdateCoordinator, entity_description: ButtonEntityDescription) -> None: ...
    async def async_press(self, **kwargs: Any) -> None: ...
