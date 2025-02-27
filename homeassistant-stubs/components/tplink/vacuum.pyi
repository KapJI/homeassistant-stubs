from . import TPLinkConfigEntry as TPLinkConfigEntry
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkModuleEntity as CoordinatedTPLinkModuleEntity, TPLinkModuleEntityDescription as TPLinkModuleEntityDescription, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.vacuum import StateVacuumEntity as StateVacuumEntity, StateVacuumEntityDescription as StateVacuumEntityDescription, VacuumActivity as VacuumActivity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from kasa import Device as Device
from kasa.smart.modules.clean import Clean as Clean
from typing import Any

PARALLEL_UPDATES: int
STATUS_TO_ACTIVITY: Incomplete

@dataclass(frozen=True, kw_only=True)
class TPLinkVacuumEntityDescription(StateVacuumEntityDescription, TPLinkModuleEntityDescription): ...

VACUUM_DESCRIPTIONS: tuple[TPLinkVacuumEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TPLinkVacuumEntity(CoordinatedTPLinkModuleEntity, StateVacuumEntity):
    _attr_supported_features: Incomplete
    entity_description: TPLinkVacuumEntityDescription
    _vacuum_module: Clean
    _speaker_module: Incomplete
    _attr_fan_speed_list: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkVacuumEntityDescription, *, parent: Device) -> None: ...
    @async_refresh_after
    async def async_start(self) -> None: ...
    @async_refresh_after
    async def async_pause(self) -> None: ...
    @async_refresh_after
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    @async_refresh_after
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    @property
    def battery_level(self) -> int | None: ...
    _attr_activity: Incomplete
    _attr_fan_speed: Incomplete
    def _async_update_attrs(self) -> bool: ...
