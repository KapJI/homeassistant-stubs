from .const import DOMAIN as DOMAIN
from .coordinator import PyLoadConfigEntry as PyLoadConfigEntry, PyLoadData as PyLoadData
from .entity import BasePyLoadEntity as BasePyLoadEntity
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyloadapi import PyLoadAPI as PyLoadAPI
from typing import Any

PARALLEL_UPDATES: int

class PyLoadSwitch(StrEnum):
    PAUSE_RESUME_QUEUE = 'download'
    RECONNECT = 'reconnect'

@dataclass(kw_only=True, frozen=True)
class PyLoadSwitchEntityDescription(SwitchEntityDescription):
    turn_on_fn: Callable[[PyLoadAPI], Awaitable[Any]]
    turn_off_fn: Callable[[PyLoadAPI], Awaitable[Any]]
    toggle_fn: Callable[[PyLoadAPI], Awaitable[Any]]
    value_fn: Callable[[PyLoadData], bool]

SENSOR_DESCRIPTIONS: tuple[PyLoadSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PyLoadConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PyLoadSwitchEntity(BasePyLoadEntity, SwitchEntity):
    entity_description: PyLoadSwitchEntityDescription
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_toggle(self, **kwargs: Any) -> None: ...
