from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry
from .entity import OpenEVSEEntity as OpenEVSEEntity
from .helpers import openevse_exception_handler as openevse_exception_handler
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from openevsehttp import OpenEVSE as OpenEVSE
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OpenEVSEButtonDescription(ButtonEntityDescription):
    press_fn: Callable[[OpenEVSE], Awaitable[Any]]

BUTTON_TYPES: tuple[OpenEVSEButtonDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSEButton(OpenEVSEEntity, ButtonEntity):
    entity_description: OpenEVSEButtonDescription
    @override
    async def async_press(self) -> None: ...
