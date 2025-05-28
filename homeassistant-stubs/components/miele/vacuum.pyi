from .const import DOMAIN as DOMAIN, MieleActions as MieleActions, MieleAppliance as MieleAppliance, PROCESS_ACTION as PROCESS_ACTION, PROGRAM_ID as PROGRAM_ID
from .coordinator import MieleConfigEntry as MieleConfigEntry
from .entity import MieleEntity as MieleEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from enum import IntEnum
from homeassistant.components.vacuum import StateVacuumEntity as StateVacuumEntity, StateVacuumEntityDescription as StateVacuumEntityDescription, VacuumActivity as VacuumActivity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pymiele import MieleEnum
from typing import Any, Final

PARALLEL_UPDATES: int
_LOGGER: Incomplete

class FanSpeed(IntEnum):
    normal = 0
    turbo = 1
    silent = 2

class FanProgram(IntEnum):
    auto = 1
    spot = 2
    turbo = 3
    silent = 4

PROGRAM_MAP: Incomplete
PROGRAM_TO_SPEED: dict[int, str]

class MieleVacuumStateCode(MieleEnum):
    idle: int
    cleaning: int
    returning: int
    paused: int
    going_to_target_area: int
    wheel_lifted: int
    dirty_sensors: int
    dust_box_missing: int
    blocked_drive_wheels: int
    blocked_brushes: int
    check_dust_box_and_filter: int
    internal_fault_reboot: int
    blocked_front_wheel: int
    docked: Incomplete
    remote_controlled: int
    missing2none: int

SUPPORTED_FEATURES: Incomplete

@dataclass(frozen=True, kw_only=True)
class MieleVacuumDescription(StateVacuumEntityDescription):
    on_value: int

@dataclass
class MieleVacuumDefinition:
    types: tuple[MieleAppliance, ...]
    description: MieleVacuumDescription

VACUUM_TYPES: Final[tuple[MieleVacuumDefinition, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: MieleConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

VACUUM_PHASE_TO_ACTIVITY: Incomplete

class MieleVacuum(MieleEntity, StateVacuumEntity):
    entity_description: MieleVacuumDescription
    _attr_supported_features = SUPPORTED_FEATURES
    _attr_fan_speed_list: Incomplete
    _attr_name: Incomplete
    @property
    def activity(self) -> VacuumActivity | None: ...
    @property
    def battery_level(self) -> int | None: ...
    @property
    def fan_speed(self) -> str | None: ...
    @property
    def available(self) -> bool: ...
    async def send(self, device_id: str, action: dict[str, Any]) -> None: ...
    async def async_clean_spot(self, **kwargs: Any) -> None: ...
    async def async_start(self, **kwargs: Any) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    async def async_pause(self, **kwargs: Any) -> None: ...
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
