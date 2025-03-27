from .const import DOMAIN as DOMAIN
from .coordinator import PyLoadConfigEntry as PyLoadConfigEntry
from .entity import BasePyLoadEntity as BasePyLoadEntity
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyloadapi import PyLoadAPI as PyLoadAPI
from typing import Any

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class PyLoadButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[PyLoadAPI], Awaitable[Any]]

class PyLoadButtonEntity(StrEnum):
    ABORT_DOWNLOADS = 'abort_downloads'
    RESTART_FAILED = 'restart_failed'
    DELETE_FINISHED = 'delete_finished'
    RESTART = 'restart'

SENSOR_DESCRIPTIONS: tuple[PyLoadButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PyLoadConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PyLoadBinarySensor(BasePyLoadEntity, ButtonEntity):
    entity_description: PyLoadButtonEntityDescription
    async def async_press(self) -> None: ...
