from . import SynoApi as SynoApi
from .coordinator import SynologyDSMCentralUpdateCoordinator as SynologyDSMCentralUpdateCoordinator, SynologyDSMConfigEntry as SynologyDSMConfigEntry
from .entity import SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMEntityDescription as SynologyDSMEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

FAN_SPEED_MAP: Incomplete
FAN_SPEED_MAP_INVERSE: Incomplete

@dataclass(frozen=True, kw_only=True)
class SynologyDSMSelectEntityDescription(SynologyDSMEntityDescription, SelectEntityDescription): ...

async def async_setup_entry(hass: HomeAssistant, entry: SynologyDSMConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SynologyDSMFanSpeedMode(SynologyDSMBaseEntity[SynologyDSMCentralUpdateCoordinator], SelectEntity):
    entity_description: SynologyDSMSelectEntityDescription
    _attr_options: Incomplete
    def __init__(self, api: SynoApi, coordinator: SynologyDSMCentralUpdateCoordinator) -> None: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
