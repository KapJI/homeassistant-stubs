import asyncio
import psutil_home_assistant as ha_psutil
import queue
import threading
from . import migration as migration, statistics as statistics
from .const import DB_WORKER_PREFIX as DB_WORKER_PREFIX, DEFAULT_MAX_BIND_VARS as DEFAULT_MAX_BIND_VARS, DOMAIN as DOMAIN, KEEPALIVE_TIME as KEEPALIVE_TIME, LAST_REPORTED_SCHEMA_VERSION as LAST_REPORTED_SCHEMA_VERSION, MARIADB_PYMYSQL_URL_PREFIX as MARIADB_PYMYSQL_URL_PREFIX, MARIADB_URL_PREFIX as MARIADB_URL_PREFIX, MAX_QUEUE_BACKLOG_MIN_VALUE as MAX_QUEUE_BACKLOG_MIN_VALUE, MIN_AVAILABLE_MEMORY_FOR_QUEUE_BACKLOG as MIN_AVAILABLE_MEMORY_FOR_QUEUE_BACKLOG, MYSQLDB_PYMYSQL_URL_PREFIX as MYSQLDB_PYMYSQL_URL_PREFIX, MYSQLDB_URL_PREFIX as MYSQLDB_URL_PREFIX, SQLITE_URL_PREFIX as SQLITE_URL_PREFIX, SupportedDialect as SupportedDialect
from .db_schema import Base as Base, EventData as EventData, EventTypes as EventTypes, Events as Events, SCHEMA_VERSION as SCHEMA_VERSION, StateAttributes as StateAttributes, States as States, StatesMeta as StatesMeta, Statistics as Statistics, StatisticsShortTerm as StatisticsShortTerm
from .executor import DBInterruptibleThreadPoolExecutor as DBInterruptibleThreadPoolExecutor
from .models import DatabaseEngine as DatabaseEngine, StatisticData as StatisticData, StatisticMetaData as StatisticMetaData, UnsupportedDialect as UnsupportedDialect
from .pool import MutexPool as MutexPool, POOL_SIZE as POOL_SIZE, RecorderPool as RecorderPool
from .table_managers.event_data import EventDataManager as EventDataManager
from .table_managers.event_types import EventTypeManager as EventTypeManager
from .table_managers.recorder_runs import RecorderRunsManager as RecorderRunsManager
from .table_managers.state_attributes import StateAttributesManager as StateAttributesManager
from .table_managers.states import StatesManager as StatesManager
from .table_managers.states_meta import StatesMetaManager as StatesMetaManager
from .table_managers.statistics_meta import StatisticsMetaManager as StatisticsMetaManager
from .tasks import AdjustLRUSizeTask as AdjustLRUSizeTask, AdjustStatisticsTask as AdjustStatisticsTask, ChangeStatisticsUnitTask as ChangeStatisticsUnitTask, ClearStatisticsTask as ClearStatisticsTask, CommitTask as CommitTask, CompileMissingStatisticsTask as CompileMissingStatisticsTask, DatabaseLockTask as DatabaseLockTask, ImportStatisticsTask as ImportStatisticsTask, KeepAliveTask as KeepAliveTask, PerodicCleanupTask as PerodicCleanupTask, PurgeTask as PurgeTask, RecorderTask as RecorderTask, StatisticsTask as StatisticsTask, StopTask as StopTask, SynchronizeTask as SynchronizeTask, UpdateStatesMetadataTask as UpdateStatesMetadataTask, UpdateStatisticsMetadataTask as UpdateStatisticsMetadataTask, WaitTask as WaitTask
from .util import async_create_backup_failure_issue as async_create_backup_failure_issue, build_mysqldb_conv as build_mysqldb_conv, dburl_to_path as dburl_to_path, end_incomplete_runs as end_incomplete_runs, is_second_sunday as is_second_sunday, move_away_broken_database as move_away_broken_database, session_scope as session_scope, setup_connection_for_dialect as setup_connection_for_dialect, validate_or_move_away_sqlite_database as validate_or_move_away_sqlite_database, write_lock_db_sqlite as write_lock_db_sqlite
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable
from datetime import datetime
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, EVENT_HOMEASSISTANT_FINAL_WRITE as EVENT_HOMEASSISTANT_FINAL_WRITE, EVENT_STATE_CHANGED as EVENT_STATE_CHANGED, MATCH_ALL as MATCH_ALL
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, EventStateChangedData as EventStateChangedData, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_track_time_change as async_track_time_change, async_track_time_interval as async_track_time_interval, async_track_utc_time_change as async_track_utc_time_change
from homeassistant.helpers.recorder import DATA_RECORDER as DATA_RECORDER
from homeassistant.helpers.start import async_at_started as async_at_started
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from homeassistant.util.event_type import EventType as EventType
from propcache.api import cached_property
from sqlalchemy.engine import Engine as Engine
from sqlalchemy.engine.interfaces import DBAPIConnection as DBAPIConnection
from sqlalchemy.orm.session import Session as Session
from typing import Any

_LOGGER: Incomplete
DEFAULT_URL: str
EXPIRE_AFTER_COMMITS: int
SHUTDOWN_TASK: Incomplete
COMMIT_TASK: Incomplete
KEEP_ALIVE_TASK: Incomplete
WAIT_TASK: Incomplete
ADJUST_LRU_SIZE_TASK: Incomplete
DB_LOCK_TIMEOUT: int
DB_LOCK_QUEUE_CHECK_TIMEOUT: int
QUEUE_CHECK_INTERVAL: Incomplete
INVALIDATED_ERR: str
CONNECTIVITY_ERR: str
MAX_DB_EXECUTOR_WORKERS: Incomplete

class Recorder(threading.Thread):
    stop_requested: bool
    hass: Incomplete
    thread_id: int | None
    recorder_and_worker_thread_ids: set[int]
    auto_purge: Incomplete
    auto_repack: Incomplete
    keep_days: Incomplete
    is_running: bool
    _hass_started: asyncio.Future[object]
    commit_interval: Incomplete
    _queue: queue.SimpleQueue[RecorderTask | Event]
    db_url: Incomplete
    db_max_retries: Incomplete
    db_retry_wait: Incomplete
    database_engine: DatabaseEngine | None
    async_db_connected: asyncio.Future[bool]
    async_db_ready: asyncio.Future[bool]
    async_recorder_ready: Incomplete
    _queue_watch: Incomplete
    engine: Engine | None
    max_backlog: int
    _psutil: ha_psutil.PsutilWrapper | None
    entity_filter: Incomplete
    exclude_event_types: Incomplete
    schema_version: int
    _commits_without_expire: int
    _event_session_has_pending_writes: bool
    recorder_runs_manager: Incomplete
    states_manager: Incomplete
    event_data_manager: Incomplete
    event_type_manager: Incomplete
    states_meta_manager: Incomplete
    state_attributes_manager: Incomplete
    statistics_meta_manager: Incomplete
    event_session: Session | None
    _get_session: Callable[[], Session] | None
    _completed_first_database_setup: bool | None
    migration_in_progress: bool
    migration_is_live: bool
    use_legacy_events_index: bool
    _database_lock_task: DatabaseLockTask | None
    _db_executor: DBInterruptibleThreadPoolExecutor | None
    _event_listener: CALLBACK_TYPE | None
    _queue_watcher: CALLBACK_TYPE | None
    _keep_alive_listener: CALLBACK_TYPE | None
    _commit_listener: CALLBACK_TYPE | None
    _periodic_listener: CALLBACK_TYPE | None
    _nightly_listener: CALLBACK_TYPE | None
    _dialect_name: SupportedDialect | None
    enabled: bool
    max_bind_vars: Incomplete
    def __init__(self, hass: HomeAssistant, auto_purge: bool, auto_repack: bool, keep_days: int, commit_interval: int, uri: str, db_max_retries: int, db_retry_wait: int, entity_filter: Callable[[str], bool] | None, exclude_event_types: set[EventType[Any] | str]) -> None: ...
    @property
    def backlog(self) -> int: ...
    @cached_property
    def dialect_name(self) -> SupportedDialect | None: ...
    @property
    def _using_file_sqlite(self) -> bool: ...
    @property
    def recording(self) -> bool: ...
    def get_session(self) -> Session: ...
    def queue_task(self, task: RecorderTask | Event) -> None: ...
    def set_enable(self, enable: bool) -> None: ...
    @callback
    def async_start_executor(self) -> None: ...
    def _shutdown_pool(self) -> None: ...
    @callback
    def async_initialize(self) -> None: ...
    @callback
    def _async_keep_alive(self, now: datetime) -> None: ...
    @callback
    def _async_commit(self, now: datetime) -> None: ...
    @callback
    def async_add_executor_job[_T](self, target: Callable[..., _T], *args: Any) -> asyncio.Future[_T]: ...
    @callback
    def _async_check_queue(self, *_: Any) -> None: ...
    def _available_memory(self) -> int: ...
    def _reached_max_backlog(self) -> bool: ...
    @callback
    def _async_stop_queue_watcher_and_event_listener(self) -> None: ...
    @callback
    def _async_stop_listeners(self) -> None: ...
    async def _async_close(self, event: Event) -> None: ...
    async def _async_shutdown(self, event: Event) -> None: ...
    @callback
    def _async_hass_started(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_register(self) -> None: ...
    @callback
    def _async_startup_done(self, startup_failed: bool) -> None: ...
    @callback
    def async_connection_success(self) -> None: ...
    @callback
    def async_set_db_ready(self) -> None: ...
    @callback
    def _async_set_recorder_ready_migration_done(self) -> None: ...
    @callback
    def async_nightly_tasks(self, now: datetime) -> None: ...
    @callback
    def _async_five_minute_tasks(self, now: datetime) -> None: ...
    def _adjust_lru_size(self) -> None: ...
    @callback
    def async_periodic_statistics(self) -> None: ...
    @callback
    def async_adjust_statistics(self, statistic_id: str, start_time: datetime, sum_adjustment: float, adjustment_unit: str) -> None: ...
    @callback
    def async_clear_statistics(self, statistic_ids: list[str], *, on_done: Callable[[], None] | None = None) -> None: ...
    @callback
    def async_update_statistics_metadata(self, statistic_id: str, *, new_statistic_id: str | UndefinedType = ..., new_unit_of_measurement: str | None | UndefinedType = ..., on_done: Callable[[], None] | None = None) -> None: ...
    @callback
    def async_update_states_metadata(self, entity_id: str, new_entity_id: str) -> None: ...
    @callback
    def async_change_statistics_unit(self, statistic_id: str, *, new_unit_of_measurement: str, old_unit_of_measurement: str) -> None: ...
    @callback
    def async_import_statistics(self, metadata: StatisticMetaData, stats: Iterable[StatisticData], table: type[Statistics | StatisticsShortTerm]) -> None: ...
    @callback
    def _async_setup_periodic_tasks(self) -> None: ...
    async def _async_wait_for_started(self) -> object | None: ...
    def _wait_startup_or_shutdown(self) -> object | None: ...
    def run(self) -> None: ...
    def _add_to_session(self, session: Session, obj: object) -> None: ...
    def _notify_migration_failed(self) -> None: ...
    def _dismiss_migration_in_progress(self) -> None: ...
    def _run(self) -> None: ...
    def _activate_and_set_db_ready(self, schema_status: migration.SchemaValidationStatus) -> None: ...
    def _run_event_loop(self) -> None: ...
    def _pre_process_startup_events(self, startup_task_or_events: list[RecorderTask | Event[Any]]) -> None: ...
    def _guarded_process_one_task_or_event_or_recover(self, task: RecorderTask | Event) -> None: ...
    def _process_one_task_or_event_or_recover(self, task: RecorderTask | Event) -> None: ...
    def _setup_recorder(self) -> bool: ...
    def _migrate_data_offline(self, schema_status: migration.SchemaValidationStatus) -> None: ...
    def _migrate_schema_offline(self, schema_status: migration.SchemaValidationStatus) -> tuple[bool, migration.SchemaValidationStatus]: ...
    def _migrate_schema_live(self, schema_status: migration.SchemaValidationStatus) -> tuple[bool, migration.SchemaValidationStatus]: ...
    def _migrate_schema(self, schema_status: migration.SchemaValidationStatus, live: bool) -> tuple[bool, migration.SchemaValidationStatus]: ...
    def _lock_database(self, task: DatabaseLockTask) -> None: ...
    def _process_one_event(self, event: Event[Any]) -> None: ...
    def _process_non_state_changed_event_into_session(self, event: Event) -> None: ...
    def _process_state_changed_event_into_session(self, event: Event[EventStateChangedData]) -> None: ...
    def _handle_database_error(self, err: Exception, *, setup_run: bool) -> bool: ...
    def _commit_event_session_or_retry(self) -> None: ...
    def _commit_event_session(self) -> None: ...
    def _handle_sqlite_corruption(self, setup_run: bool) -> None: ...
    def _close_event_session(self) -> None: ...
    def _reopen_event_session(self) -> None: ...
    def _open_event_session(self) -> None: ...
    def _send_keep_alive(self) -> None: ...
    async def async_block_till_done(self) -> None: ...
    def block_till_done(self) -> None: ...
    async def lock_database(self) -> bool: ...
    @callback
    def unlock_database(self) -> bool: ...
    def _setup_recorder_connection(self, dbapi_connection: DBAPIConnection, connection_record: Any) -> None: ...
    def _setup_connection(self) -> None: ...
    def _close_connection(self) -> None: ...
    def _setup_run(self) -> None: ...
    def _schedule_compile_missing_statistics(self) -> None: ...
    def _end_session(self) -> None: ...
    def _shutdown(self) -> None: ...
