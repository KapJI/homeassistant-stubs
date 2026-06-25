from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityDescription as FanEntityDescription, FanEntityFeature as FanEntityFeature
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyoverkiz.enums import OverkizCommand, OverkizState
from typing import Any, override

@dataclass(frozen=True, kw_only=True)
class OverkizFanDescription(FanEntityDescription):
    percentage: OverkizState
    set_percentage: OverkizCommand

FAN_DESCRIPTIONS: list[OverkizFanDescription]
SUPPORTED_DEVICES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OverkizFan(OverkizDescriptiveEntity, FanEntity):
    entity_description: OverkizFanDescription
    _attr_supported_features: Incomplete
    @property
    @override
    def percentage(self) -> int | None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    async def async_set_percentage(self, percentage: int) -> None: ...
    @override
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
