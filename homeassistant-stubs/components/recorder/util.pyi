from . import Recorder as Recorder
from .const import DATA_INSTANCE as DATA_INSTANCE, DEFAULT_MAX_BIND_VARS as DEFAULT_MAX_BIND_VARS, DOMAIN as DOMAIN, SQLITE_MAX_BIND_VARS as SQLITE_MAX_BIND_VARS, SQLITE_MODERN_MAX_BIND_VARS as SQLITE_MODERN_MAX_BIND_VARS, SQLITE_URL_PREFIX as SQLITE_URL_PREFIX, SupportedDialect as SupportedDialect
from .db_schema import RecorderRuns as RecorderRuns, TABLES_TO_CHECK as TABLES_TO_CHECK, TABLE_RECORDER_RUNS as TABLE_RECORDER_RUNS, TABLE_SCHEMA_CHANGES as TABLE_SCHEMA_CHANGES
from .models import DatabaseEngine as DatabaseEngine, DatabaseOptimizer as DatabaseOptimizer, StatisticPeriod as StatisticPeriod, UnsupportedDialect as UnsupportedDialect, process_timestamp as process_timestamp
from _typeshed import Incomplete
from awesomeversion import AwesomeVersion
from collections.abc import Callable, Generator, Iterable, Sequence
from datetime import date, datetime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from sqlalchemy.engine import Result as Result, Row as Row
from sqlalchemy.engine.interfaces import DBAPIConnection as DBAPIConnection
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.query import Query as Query
from sqlalchemy.orm.session import Session as Session
from sqlalchemy.sql.lambdas import StatementLambdaElement as StatementLambdaElement
from sqlite3.dbapi2 import Cursor as SQLiteCursor
from typing import Any, NoReturn, TypeVar

_RecorderT = TypeVar('_RecorderT', bound='Recorder')
_P: Incomplete
_LOGGER: Incomplete
RETRIES: int
QUERY_RETRY_WAIT: float
SQLITE3_POSTFIXES: Incomplete
DEFAULT_YIELD_STATES_ROWS: int

def _simple_version(version: str) -> AwesomeVersion: ...

MIN_VERSION_MARIA_DB: Incomplete
RECOMMENDED_MIN_VERSION_MARIA_DB: Incomplete
MARIADB_WITH_FIXED_IN_QUERIES_105: Incomplete
MARIA_DB_106: Incomplete
MARIADB_WITH_FIXED_IN_QUERIES_106: Incomplete
RECOMMENDED_MIN_VERSION_MARIA_DB_106: Incomplete
MARIA_DB_107: Incomplete
RECOMMENDED_MIN_VERSION_MARIA_DB_107: Incomplete
MARIADB_WITH_FIXED_IN_QUERIES_107: Incomplete
MARIA_DB_108: Incomplete
RECOMMENDED_MIN_VERSION_MARIA_DB_108: Incomplete
MARIADB_WITH_FIXED_IN_QUERIES_108: Incomplete
MIN_VERSION_MYSQL: Incomplete
MIN_VERSION_PGSQL: Incomplete
MIN_VERSION_SQLITE: Incomplete
MIN_VERSION_SQLITE_MODERN_BIND_VARS: Incomplete
MAX_RESTART_TIME: Incomplete
RETRYABLE_MYSQL_ERRORS: Incomplete
FIRST_POSSIBLE_SUNDAY: int
SUNDAY_WEEKDAY: int
DAYS_IN_WEEK: int

def session_scope(*, hass: HomeAssistant | None = ..., session: Session | None = ..., exception_filter: Callable[[Exception], bool] | None = ..., read_only: bool = ...) -> Generator[Session, None, None]: ...
def execute(qry: Query, to_native: bool = ..., validate_entity_ids: bool = ...) -> list[Row]: ...
def execute_stmt_lambda_element(session: Session, stmt: StatementLambdaElement, start_time: datetime | None = ..., end_time: datetime | None = ..., yield_per: int = ..., orm_rows: bool = ...) -> Sequence[Row] | Result: ...
def validate_or_move_away_sqlite_database(dburl: str) -> bool: ...
def dburl_to_path(dburl: str) -> str: ...
def last_run_was_recently_clean(cursor: SQLiteCursor) -> bool: ...
def basic_sanity_check(cursor: SQLiteCursor) -> bool: ...
def validate_sqlite_database(dbpath: str) -> bool: ...
def run_checks_on_open_db(dbpath: str, cursor: SQLiteCursor) -> None: ...
def move_away_broken_database(dbfile: str) -> None: ...
def execute_on_connection(dbapi_connection: DBAPIConnection, statement: str) -> None: ...
def query_on_connection(dbapi_connection: DBAPIConnection, statement: str) -> Any: ...
def _fail_unsupported_dialect(dialect_name: str) -> NoReturn: ...
def _fail_unsupported_version(server_version: str, dialect_name: str, minimum_version: str) -> NoReturn: ...
def _extract_version_from_server_response(server_response: str) -> AwesomeVersion | None: ...
def _datetime_or_none(value: str) -> datetime | None: ...
def build_mysqldb_conv() -> dict: ...
def _async_create_mariadb_range_index_regression_issue(hass: HomeAssistant, version: AwesomeVersion) -> None: ...
def setup_connection_for_dialect(instance: Recorder, dialect_name: str, dbapi_connection: DBAPIConnection, first_connection: bool) -> DatabaseEngine | None: ...
def end_incomplete_runs(session: Session, start_time: datetime) -> None: ...
def _is_retryable_error(instance: Recorder, err: OperationalError) -> bool: ...

_FuncType: Incomplete

def retryable_database_job(description: str) -> Callable[[_FuncType[_RecorderT, _P]], _FuncType[_RecorderT, _P]]: ...

_WrappedFuncType: Incomplete

def database_job_retry_wrapper(description: str, attempts: int = ...) -> Callable[[_WrappedFuncType[_RecorderT, _P]], _WrappedFuncType[_RecorderT, _P]]: ...
def periodic_db_cleanups(instance: Recorder) -> None: ...
def write_lock_db_sqlite(instance: Recorder) -> Generator[None, None, None]: ...
def async_migration_in_progress(hass: HomeAssistant) -> bool: ...
def async_migration_is_live(hass: HomeAssistant) -> bool: ...
def second_sunday(year: int, month: int) -> date: ...
def is_second_sunday(date_time: datetime) -> bool: ...
def get_instance(hass: HomeAssistant) -> Recorder: ...

PERIOD_SCHEMA: Incomplete

def resolve_period(period_def: StatisticPeriod) -> tuple[datetime | None, datetime | None]: ...
def take(take_num: int, iterable: Iterable) -> list[Any]: ...
def chunked(iterable: Iterable, chunked_num: int) -> Iterable[Any]: ...
def get_index_by_name(session: Session, table_name: str, index_name: str) -> str | None: ...
