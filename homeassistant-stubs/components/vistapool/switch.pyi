from . import VistapoolConfigEntry as VistapoolConfigEntry
from .const import DOMAIN as DOMAIN, PATH_HASHIDRO as PATH_HASHIDRO, SIGNAL_NEW_POOL as SIGNAL_NEW_POOL
from .coordinator import VistapoolDataUpdateCoordinator as VistapoolDataUpdateCoordinator
from .entity import VistapoolEntity as VistapoolEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class VistapoolSwitchEntityDescription(SwitchEntityDescription):
    value_path: str
    extra_read_paths: tuple[str, ...] = ...
    exists_path: str | tuple[str, ...] | None = ...

SWITCH_DESCRIPTIONS: tuple[VistapoolSwitchEntityDescription, ...]

def _build_switch_entities(coordinator: VistapoolDataUpdateCoordinator) -> list[SwitchEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: VistapoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VistapoolSwitch(VistapoolEntity, SwitchEntity):
    entity_description: VistapoolSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VistapoolDataUpdateCoordinator, description: VistapoolSwitchEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_set_value(self, value: int) -> None: ...
