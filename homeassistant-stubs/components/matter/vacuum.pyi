from .entity import MatterEntity as MatterEntity, MatterEntityDescription as MatterEntityDescription
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters import Objects as clusters
from dataclasses import dataclass
from enum import IntEnum
from homeassistant.components.vacuum import StateVacuumEntity as StateVacuumEntity, StateVacuumEntityDescription as StateVacuumEntityDescription, VacuumActivity as VacuumActivity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

class OperationalState(IntEnum):
    STOPPED = 0
    RUNNING = 1
    PAUSED = 2
    ERROR = 3
    SEEKING_CHARGER = 64
    CHARGING = 65
    DOCKED = 66

class ModeTag(IntEnum):
    IDLE = 16384
    CLEANING = 16385
    MAPPING = 16386

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

@dataclass(frozen=True, kw_only=True)
class MatterStateVacuumEntityDescription(StateVacuumEntityDescription, MatterEntityDescription): ...

class MatterVacuum(MatterEntity, StateVacuumEntity):
    _last_accepted_commands: list[int] | None
    _supported_run_modes: dict[int, clusters.RvcRunMode.Structs.ModeOptionStruct] | None
    entity_description: MatterStateVacuumEntityDescription
    _platform_translation_key: str
    def _get_run_mode_by_tag(self, tag: ModeTag) -> clusters.RvcRunMode.Structs.ModeOptionStruct | None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    async def async_start(self) -> None: ...
    async def async_pause(self) -> None: ...
    _attr_activity: Incomplete
    @callback
    def _update_from_device(self) -> None: ...
    _attr_supported_features: Incomplete
    @callback
    def _calculate_features(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
