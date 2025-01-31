from .core import Recorder as Recorder
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, ATTR_RESTORED as ATTR_RESTORED, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, EVENT_RECORDER_5MIN_STATISTICS_GENERATED as EVENT_RECORDER_5MIN_STATISTICS_GENERATED, EVENT_RECORDER_HOURLY_STATISTICS_GENERATED as EVENT_RECORDER_HOURLY_STATISTICS_GENERATED
from homeassistant.helpers.json import JSON_DUMP as JSON_DUMP

SQLITE_URL_PREFIX: str
MARIADB_URL_PREFIX: str
MARIADB_PYMYSQL_URL_PREFIX: str
MYSQLDB_URL_PREFIX: str
MYSQLDB_PYMYSQL_URL_PREFIX: str
DOMAIN: str
CONF_DB_INTEGRITY_CHECK: str
MAX_QUEUE_BACKLOG_MIN_VALUE: int
MIN_AVAILABLE_MEMORY_FOR_QUEUE_BACKLOG: Incomplete
DEFAULT_MAX_BIND_VARS: int
DB_WORKER_PREFIX: str
ALL_DOMAIN_EXCLUDE_ATTRS: Incomplete
ATTR_KEEP_DAYS: str
ATTR_REPACK: str
ATTR_APPLY_FILTER: str
KEEPALIVE_TIME: int
CONTEXT_ID_AS_BINARY_SCHEMA_VERSION: int
EVENT_TYPE_IDS_SCHEMA_VERSION: int
STATES_META_SCHEMA_VERSION: int
LAST_REPORTED_SCHEMA_VERSION: int
LEGACY_STATES_EVENT_ID_INDEX_SCHEMA_VERSION: int
INTEGRATION_PLATFORM_COMPILE_STATISTICS: str
INTEGRATION_PLATFORM_LIST_STATISTIC_IDS: str
INTEGRATION_PLATFORM_UPDATE_STATISTICS_ISSUES: str
INTEGRATION_PLATFORM_VALIDATE_STATISTICS: str
INTEGRATION_PLATFORM_METHODS: Incomplete

class SupportedDialect(StrEnum):
    SQLITE = 'sqlite'
    MYSQL = 'mysql'
    POSTGRESQL = 'postgresql'
