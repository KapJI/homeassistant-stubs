from . import AirGradientConfigEntry as AirGradientConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AirGradientCoordinator as AirGradientCoordinator
from .entity import AirGradientEntity as AirGradientEntity, exception_handler as exception_handler
from _typeshed import Incomplete
from airgradient import AirGradientClient as AirGradientClient, Config as Config
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class AirGradientSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[Config], bool]
    set_value_fn: Callable[[AirGradientClient, bool], Awaitable[None]]

POST_DATA_TO_AIRGRADIENT: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AirGradientConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirGradientSwitch(AirGradientEntity, SwitchEntity):
    entity_description: AirGradientSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirGradientCoordinator, description: AirGradientSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @exception_handler
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @exception_handler
    async def async_turn_off(self, **kwargs: Any) -> None: ...
