from . import EcovacsConfigEntry as EcovacsConfigEntry
from .entity import EcovacsCapabilityEntityDescription as EcovacsCapabilityEntityDescription, EcovacsDescriptionEntity as EcovacsDescriptionEntity, EcovacsEntity as EcovacsEntity
from .util import get_name_key as get_name_key, get_supported_entities as get_supported_entities
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from deebot_client.capabilities import CapabilityMap, CapabilitySetTypes
from deebot_client.command import CommandWithMessageHandling as CommandWithMessageHandling
from deebot_client.device import Device as Device
from deebot_client.events.base import Event as Event
from deebot_client.events.map import CachedMapInfoEvent, MajorMapEvent as MajorMapEvent
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

@dataclass(kw_only=True, frozen=True)
class EcovacsSelectEntityDescription[EventT: Event](SelectEntityDescription, EcovacsCapabilityEntityDescription):
    current_option_fn: Callable[[EventT], str | None]
    options_fn: Callable[[CapabilitySetTypes], list[str]]
    set_option_fn: Callable[[CapabilitySetTypes, str], CommandWithMessageHandling] = ...

ENTITY_DESCRIPTIONS: tuple[EcovacsSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EcovacsSelectEntity[EventT: Event](EcovacsDescriptionEntity[CapabilitySetTypes[EventT, [str], str]], SelectEntity):
    _attr_current_option: str | None
    entity_description: EcovacsSelectEntityDescription
    _attr_options: Incomplete
    def __init__(self, device: Device, capability: CapabilitySetTypes[EventT, [str], str], entity_description: EcovacsSelectEntityDescription, **kwargs: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...

class EcovacsActiveMapSelectEntity(EcovacsEntity[CapabilityMap], SelectEntity):
    entity_description: Incomplete
    _option_to_id: dict[str, str]
    _id_to_option: dict[str, str]
    def __init__(self, device: Device, capability: CapabilityMap, **kwargs: Any) -> None: ...
    _attr_current_option: Incomplete
    _attr_options: Incomplete
    def _handle_on_cached_map(self, event: CachedMapInfoEvent) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
