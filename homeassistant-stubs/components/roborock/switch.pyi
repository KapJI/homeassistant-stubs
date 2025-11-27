from .const import DOMAIN as DOMAIN
from .coordinator import RoborockConfigEntry as RoborockConfigEntry, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from roborock.devices.traits.v1 import PropertiesApi as PropertiesApi
from roborock.devices.traits.v1.common import RoborockSwitchBase as RoborockSwitchBase
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockSwitchDescription(SwitchEntityDescription):
    trait: Callable[[PropertiesApi], RoborockSwitchBase | None]
    is_dock_entity: bool = ...

SWITCH_DESCRIPTIONS: list[RoborockSwitchDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockSwitch(RoborockEntityV1, SwitchEntity):
    entity_description: RoborockSwitchDescription
    _trait: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockSwitchDescription, trait: RoborockSwitchBase) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
