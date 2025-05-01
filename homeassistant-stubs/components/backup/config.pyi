import datetime as dt
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .manager import BackupManager as BackupManager, ManagerBackup as ManagerBackup
from .models import BackupManagerError as BackupManagerError, Folder as Folder
from _typeshed import Incomplete
from cronsim import CronSim
from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_point_in_time as async_track_point_in_time
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from typing import Self, TypedDict

AUTOMATIC_BACKUP_AGENTS_UNAVAILABLE_ISSUE_ID: str
CRON_PATTERN_DAILY: str
CRON_PATTERN_WEEKLY: str
DEFAULT_BACKUP_TIME: Incomplete
BACKUP_START_TIME_JITTER: Incomplete

class StoredBackupConfig(TypedDict):
    agents: dict[str, StoredAgentConfig]
    automatic_backups_configured: bool
    create_backup: StoredCreateBackupConfig
    last_attempted_automatic_backup: str | None
    last_completed_automatic_backup: str | None
    retention: StoredRetentionConfig
    schedule: StoredBackupSchedule

@dataclass(kw_only=True)
class BackupConfigData:
    agents: dict[str, AgentConfig]
    automatic_backups_configured: bool
    create_backup: CreateBackupConfig
    last_attempted_automatic_backup: datetime | None = ...
    last_completed_automatic_backup: datetime | None = ...
    retention: RetentionConfig
    schedule: BackupSchedule
    @classmethod
    def from_dict(cls, data: StoredBackupConfig) -> Self: ...
    def to_dict(self) -> StoredBackupConfig: ...

class BackupConfig:
    data: Incomplete
    _hass: Incomplete
    _manager: Incomplete
    def __init__(self, hass: HomeAssistant, manager: BackupManager) -> None: ...
    def load(self, stored_config: StoredBackupConfig) -> None: ...
    @callback
    def update(self, *, agents: dict[str, AgentParametersDict] | UndefinedType = ..., automatic_backups_configured: bool | UndefinedType = ..., create_backup: CreateBackupParametersDict | UndefinedType = ..., retention: RetentionParametersDict | UndefinedType = ..., schedule: ScheduleParametersDict | UndefinedType = ...) -> None: ...

@dataclass(kw_only=True)
class AgentConfig:
    protected: bool
    retention: AgentRetentionConfig | None = ...
    def to_dict(self) -> StoredAgentConfig: ...

class StoredAgentConfig(TypedDict):
    protected: bool
    retention: StoredRetentionConfig | None

class AgentParametersDict(TypedDict, total=False):
    protected: bool
    retention: RetentionParametersDict | None

@dataclass(kw_only=True)
class BaseRetentionConfig:
    copies: int | None = ...
    days: int | None = ...
    def to_dict(self) -> StoredRetentionConfig: ...

@dataclass(kw_only=True)
class RetentionConfig(BaseRetentionConfig):
    def apply(self, manager: BackupManager) -> None: ...
    @callback
    def _schedule_next(self, manager: BackupManager) -> None: ...
    @callback
    def _unschedule_next(self, manager: BackupManager) -> None: ...

class StoredRetentionConfig(TypedDict):
    copies: int | None
    days: int | None

class RetentionParametersDict(TypedDict, total=False):
    copies: int | None
    days: int | None

class AgentRetentionConfig(BaseRetentionConfig): ...

class StoredBackupSchedule(TypedDict):
    days: list[Day]
    recurrence: ScheduleRecurrence
    state: ScheduleState
    time: str | None

class ScheduleParametersDict(TypedDict, total=False):
    days: list[Day]
    recurrence: ScheduleRecurrence
    state: ScheduleState
    time: dt.time | None

class Day(StrEnum):
    MONDAY = 'mon'
    TUESDAY = 'tue'
    WEDNESDAY = 'wed'
    THURSDAY = 'thu'
    FRIDAY = 'fri'
    SATURDAY = 'sat'
    SUNDAY = 'sun'

class ScheduleRecurrence(StrEnum):
    NEVER = 'never'
    DAILY = 'daily'
    CUSTOM_DAYS = 'custom_days'

class ScheduleState(StrEnum):
    NEVER = 'never'
    DAILY = 'daily'
    MONDAY = 'mon'
    TUESDAY = 'tue'
    WEDNESDAY = 'wed'
    THURSDAY = 'thu'
    FRIDAY = 'fri'
    SATURDAY = 'sat'
    SUNDAY = 'sun'

@dataclass(kw_only=True)
class BackupSchedule:
    days: list[Day] = field(default_factory=list)
    recurrence: ScheduleRecurrence = ...
    state: ScheduleState = ...
    time: dt.time | None = ...
    cron_event: CronSim | None = field(init=False, default=None)
    next_automatic_backup: datetime | None = field(init=False, default=None)
    next_automatic_backup_additional = ...
    @callback
    def apply(self, manager: BackupManager) -> None: ...
    @callback
    def _schedule_next(self, cron_pattern: str, manager: BackupManager) -> None: ...
    def to_dict(self) -> StoredBackupSchedule: ...
    @callback
    def _unschedule_next(self, manager: BackupManager) -> None: ...

@dataclass(kw_only=True)
class CreateBackupConfig:
    agent_ids: list[str] = field(default_factory=list)
    include_addons: list[str] | None = ...
    include_all_addons: bool = ...
    include_database: bool = ...
    include_folders: list[Folder] | None = ...
    name: str | None = ...
    password: str | None = ...
    def to_dict(self) -> StoredCreateBackupConfig: ...

class StoredCreateBackupConfig(TypedDict):
    agent_ids: list[str]
    include_addons: list[str] | None
    include_all_addons: bool
    include_database: bool
    include_folders: list[Folder] | None
    name: str | None
    password: str | None

class CreateBackupParametersDict(TypedDict, total=False):
    agent_ids: list[str]
    include_addons: list[str] | None
    include_all_addons: bool
    include_database: bool
    include_folders: list[Folder] | None
    name: str | None
    password: str | None

def _automatic_backups_filter(backups: dict[str, ManagerBackup]) -> dict[str, ManagerBackup]: ...
async def delete_backups_exceeding_configured_count(manager: BackupManager) -> None: ...
@callback
def check_unavailable_agents(hass: HomeAssistant, manager: BackupManager) -> None: ...
