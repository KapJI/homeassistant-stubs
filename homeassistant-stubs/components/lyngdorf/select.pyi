from .entity import LyngdorfEntity as LyngdorfEntity
from .models import LyngdorfConfigEntry as LyngdorfConfigEntry
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from lyngdorf import LyngdorfReceiver as LyngdorfReceiver
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LyngdorfSelectEntityDescription(SelectEntityDescription):
    current_option_fn: Callable[[LyngdorfReceiver], str | None]
    options_fn: Callable[[LyngdorfReceiver], list[str]]
    select_option_fn: Callable[[LyngdorfReceiver, str], Awaitable[None]]

SELECT_ENTITIES: tuple[LyngdorfSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: LyngdorfConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LyngdorfSelect(LyngdorfEntity, SelectEntity):
    entity_description: LyngdorfSelectEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, receiver: LyngdorfReceiver, config_entry: LyngdorfConfigEntry, device_info: DeviceInfo, description: LyngdorfSelectEntityDescription) -> None: ...
    @override
    @property
    def current_option(self) -> str | None: ...
    @override
    @property
    def options(self) -> list[str]: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
