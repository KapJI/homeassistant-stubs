import asyncio
from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry
from .entity import OpenEVSEEntity as OpenEVSEEntity
from .helpers import openevse_exception_handler as openevse_exception_handler
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from openevsehttp import OpenEVSE as OpenEVSE
from typing import Any, override

PARALLEL_UPDATES: int
OVERRIDE_STATE_OPTIONS: list[str]

async def _async_set_override_state(charger: OpenEVSE, option: str) -> None: ...

@dataclass(frozen=True, kw_only=True)
class OpenEVSESelectDescription(SelectEntityDescription):
    current_option_fn: Callable[[OpenEVSE], Awaitable[str | None]]
    select_option_fn: Callable[[OpenEVSE, str], Awaitable[Any]]

SELECT_TYPES: tuple[OpenEVSESelectDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSESelect(OpenEVSEEntity, SelectEntity):
    entity_description: OpenEVSESelectDescription
    _attr_current_option: str | None
    _update_task: asyncio.Task[None] | None
    @property
    @override
    def available(self) -> bool: ...
    async def _async_update_current_option(self) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    def _handle_coordinator_update(self) -> None: ...
    async def _async_update_and_write_ha_state(self) -> None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
