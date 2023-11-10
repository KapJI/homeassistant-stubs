import abc
import asyncio
import threading
from . import entity_registry as entity_registry, purge as purge, statistics as statistics
from .const import DOMAIN as DOMAIN
from .core import Recorder as Recorder
from .db_schema import Statistics as Statistics, StatisticsShortTerm as StatisticsShortTerm
from .models import StatisticData as StatisticData, StatisticMetaData as StatisticMetaData
from .util import periodic_db_cleanups as periodic_db_cleanups, session_scope as session_scope
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.core import Event as Event
from homeassistant.helpers.typing import UndefinedType as UndefinedType
from typing import Any

_LOGGER: Incomplete

@dataclass(slots=True)
class RecorderTask(metaclass=abc.ABCMeta):
    commit_before = ...
    @abc.abstractmethod
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class ChangeStatisticsUnitTask(RecorderTask):
    statistic_id: str
    new_unit_of_measurement: str
    old_unit_of_measurement: str
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, statistic_id, new_unit_of_measurement, old_unit_of_measurement) -> None: ...

@dataclass(slots=True)
class ClearStatisticsTask(RecorderTask):
    statistic_ids: list[str]
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, statistic_ids) -> None: ...

@dataclass(slots=True)
class UpdateStatisticsMetadataTask(RecorderTask):
    statistic_id: str
    new_statistic_id: str | None | UndefinedType
    new_unit_of_measurement: str | None | UndefinedType
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, statistic_id, new_statistic_id, new_unit_of_measurement) -> None: ...

@dataclass(slots=True)
class UpdateStatesMetadataTask(RecorderTask):
    entity_id: str
    new_entity_id: str
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, entity_id, new_entity_id) -> None: ...

@dataclass(slots=True)
class PurgeTask(RecorderTask):
    purge_before: datetime
    repack: bool
    apply_filter: bool
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, purge_before, repack, apply_filter) -> None: ...

@dataclass(slots=True)
class PurgeEntitiesTask(RecorderTask):
    entity_filter: Callable[[str], bool]
    purge_before: datetime
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, entity_filter, purge_before) -> None: ...

@dataclass(slots=True)
class PerodicCleanupTask(RecorderTask):
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class StatisticsTask(RecorderTask):
    start: datetime
    fire_events: bool
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, start, fire_events) -> None: ...

@dataclass(slots=True)
class CompileMissingStatisticsTask(RecorderTask):
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class ImportStatisticsTask(RecorderTask):
    metadata: StatisticMetaData
    statistics: Iterable[StatisticData]
    table: type[Statistics | StatisticsShortTerm]
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, metadata, statistics, table) -> None: ...

@dataclass(slots=True)
class AdjustStatisticsTask(RecorderTask):
    statistic_id: str
    start_time: datetime
    sum_adjustment: float
    adjustment_unit: str
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, statistic_id, start_time, sum_adjustment, adjustment_unit) -> None: ...

@dataclass(slots=True)
class WaitTask(RecorderTask):
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class DatabaseLockTask(RecorderTask):
    database_locked: asyncio.Event
    database_unlock: threading.Event
    queue_overflow: bool
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, database_locked, database_unlock, queue_overflow) -> None: ...

@dataclass(slots=True)
class StopTask(RecorderTask):
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class EventTask(RecorderTask):
    event: Event
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, event) -> None: ...

@dataclass(slots=True)
class KeepAliveTask(RecorderTask):
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class CommitTask(RecorderTask):
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class AddRecorderPlatformTask(RecorderTask):
    domain: str
    platform: Any
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, domain, platform) -> None: ...

@dataclass(slots=True)
class SynchronizeTask(RecorderTask):
    event: asyncio.Event
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, event) -> None: ...

@dataclass(slots=True)
class PostSchemaMigrationTask(RecorderTask):
    old_version: int
    new_version: int
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, old_version, new_version) -> None: ...

@dataclass(slots=True)
class StatisticsTimestampMigrationCleanupTask(RecorderTask):
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class AdjustLRUSizeTask(RecorderTask):
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class StatesContextIDMigrationTask(RecorderTask):
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class EventsContextIDMigrationTask(RecorderTask):
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class EventTypeIDMigrationTask(RecorderTask):
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class EntityIDMigrationTask(RecorderTask):
    commit_before = ...
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class EntityIDPostMigrationTask(RecorderTask):
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class EventIdMigrationTask(RecorderTask):
    def run(self, instance: Recorder) -> None: ...

@dataclass(slots=True)
class RefreshEventTypesTask(RecorderTask):
    event_types: list[str]
    def run(self, instance: Recorder) -> None: ...
    def __init__(self, event_types) -> None: ...
