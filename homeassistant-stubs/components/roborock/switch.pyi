from .const import DOMAIN as DOMAIN
from .coordinator import RoborockB01Q10UpdateCoordinator as RoborockB01Q10UpdateCoordinator, RoborockConfigEntry as RoborockConfigEntry, RoborockCoordinatorType as RoborockCoordinatorType, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01
from .entity import RoborockCoordinatedEntityA01 as RoborockCoordinatedEntityA01, RoborockCoordinatedEntityB01Q10 as RoborockCoordinatedEntityB01Q10, RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from roborock.devices.traits.b01 import Q10PropertiesApi as Q10PropertiesApi
from roborock.devices.traits.b01.q10 import ButtonLightTrait as ButtonLightTrait, ChildLockTrait, DoNotDisturbTrait, DustCollectionTrait
from roborock.devices.traits.v1 import PropertiesApi as PropertiesApi
from roborock.devices.traits.v1.common import RoborockSwitchBase as RoborockSwitchBase
from roborock.roborock_message import RoborockDyadDataProtocol as RoborockDyadDataProtocol, RoborockZeoProtocol
from typing import Any, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RoborockSwitchDescription(SwitchEntityDescription):
    trait: Callable[[PropertiesApi], RoborockSwitchBase | None]
    is_dock_entity: bool = ...

SWITCH_DESCRIPTIONS: list[RoborockSwitchDescription]

@dataclass(frozen=True, kw_only=True)
class RoborockSwitchDescriptionA01(SwitchEntityDescription):
    data_protocol: RoborockDyadDataProtocol | RoborockZeoProtocol
type Q10SwitchTrait = ChildLockTrait | DoNotDisturbTrait | DustCollectionTrait

@dataclass(frozen=True, kw_only=True)
class RoborockSwitchDescriptionQ10(SwitchEntityDescription):
    trait: Callable[[Q10PropertiesApi], Q10SwitchTrait | None]

A01_SWITCH_DESCRIPTIONS: list[RoborockSwitchDescriptionA01]
Q10_SWITCH_DESCRIPTIONS: list[RoborockSwitchDescriptionQ10]

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockSwitch(RoborockEntityV1, SwitchEntity):
    entity_description: RoborockSwitchDescription
    _trait: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockSwitchDescription, trait: RoborockSwitchBase) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...

class RoborockSwitchA01(RoborockCoordinatedEntityA01, SwitchEntity):
    entity_description: RoborockSwitchDescriptionA01
    def __init__(self, coordinator: RoborockDataUpdateCoordinatorA01, description: RoborockSwitchDescriptionA01) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...

class RoborockSwitchQ10(RoborockCoordinatedEntityB01Q10, SwitchEntity):
    entity_description: RoborockSwitchDescriptionQ10
    coordinator: RoborockB01Q10UpdateCoordinator
    _trait: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockB01Q10UpdateCoordinator, description: RoborockSwitchDescriptionQ10, trait: Q10SwitchTrait) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...

class RoborockSwitchQ10ButtonLight(RoborockCoordinatedEntityB01Q10, SwitchEntity, RestoreEntity):
    _attr_assumed_state: bool
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _trait: Incomplete
    def __init__(self, unique_id: str, coordinator: RoborockB01Q10UpdateCoordinator, trait: ButtonLightTrait) -> None: ...
    _attr_is_on: Incomplete
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
