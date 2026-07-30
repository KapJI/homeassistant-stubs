from .const import DOMAIN as DOMAIN
from .coordinator import RoborockB01Q10UpdateCoordinator as RoborockB01Q10UpdateCoordinator, RoborockConfigEntry as RoborockConfigEntry, RoborockCoordinatorType as RoborockCoordinatorType, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockCoordinatedEntityB01Q10 as RoborockCoordinatedEntityB01Q10, RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from roborock.devices.traits.b01 import Q10PropertiesApi as Q10PropertiesApi
from roborock.devices.traits.b01.q10 import SoundVolumeTrait as SoundVolumeTrait
from roborock.devices.traits.v1 import PropertiesApi as PropertiesApi
from typing import Any, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockNumberDescription(NumberEntityDescription):
    trait: Callable[[PropertiesApi], Any | None]
    get_value: Callable[[Any], float | None]
    set_value: Callable[[Any, float], Coroutine[Any, Any, None]]

NUMBER_DESCRIPTIONS: list[RoborockNumberDescription]

@dataclass(frozen=True, kw_only=True)
class RoborockNumberDescriptionQ10(NumberEntityDescription):
    trait: Callable[[Q10PropertiesApi], SoundVolumeTrait | None]
    get_value: Callable[[SoundVolumeTrait], float | None]
    set_value: Callable[[SoundVolumeTrait, float], Coroutine[Any, Any, None]]

Q10_NUMBER_DESCRIPTIONS: list[RoborockNumberDescriptionQ10]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockNumberEntity(RoborockEntityV1, NumberEntity):
    entity_description: RoborockNumberDescription
    _trait: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockNumberDescription, trait: Any) -> None: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...

class RoborockNumberEntityQ10(RoborockCoordinatedEntityB01Q10, NumberEntity):
    entity_description: RoborockNumberDescriptionQ10
    coordinator: RoborockB01Q10UpdateCoordinator
    _trait: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockB01Q10UpdateCoordinator, entity_description: RoborockNumberDescriptionQ10, trait: SoundVolumeTrait) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...
