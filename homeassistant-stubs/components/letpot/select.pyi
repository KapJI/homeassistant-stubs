from .coordinator import LetPotConfigEntry as LetPotConfigEntry, LetPotDeviceCoordinator as LetPotDeviceCoordinator
from .entity import LetPotEntity as LetPotEntity, LetPotEntityDescription as LetPotEntityDescription, exception_handler as exception_handler
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from letpot.deviceclient import LetPotDeviceClient as LetPotDeviceClient
from letpot.models import LetPotDeviceStatus as LetPotDeviceStatus, LetPotGardenStatus
from typing import Any, override

PARALLEL_UPDATES: int

class LightBrightnessLowHigh(StrEnum):
    LOW = 'low'
    HIGH = 'high'

def _get_brightness_low_high_value(coordinator: LetPotDeviceCoordinator) -> str | None: ...
async def _set_brightness_low_high_value(device_client: LetPotDeviceClient, serial: str, option: str) -> None: ...

@dataclass(frozen=True, kw_only=True)
class LetPotSelectEntityDescription[_DataT: LetPotDeviceStatus](LetPotEntityDescription, SelectEntityDescription):
    value_fn: Callable[[LetPotDeviceCoordinator[_DataT]], str | None]
    set_value_fn: Callable[[LetPotDeviceClient, str, str], Coroutine[Any, Any, None]]

SELECTORS: tuple[LetPotSelectEntityDescription[LetPotGardenStatus], ...]

async def async_setup_entry(hass: HomeAssistant, entry: LetPotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LetPotSelectEntity[_DataT: LetPotDeviceStatus](LetPotEntity[_DataT], SelectEntity):
    entity_description: LetPotSelectEntityDescription[_DataT]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LetPotDeviceCoordinator[_DataT], description: LetPotSelectEntityDescription[_DataT]) -> None: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @exception_handler
    @override
    async def async_select_option(self, option: str) -> None: ...
