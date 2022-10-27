from _typeshed import Incomplete
from enum import Enum

DOMAIN: str
DEVICE_AUTH_IMPL: str
CONF_CALENDAR_ACCESS: str
DATA_CALENDARS: str
DATA_SERVICE: str
DATA_CONFIG: str
DATA_STORE: str

class FeatureAccess(Enum):
    read_only: str
    read_write: str
    _scope: Incomplete
    def __init__(self, scope: str) -> None: ...
    @property
    def scope(self) -> str: ...

DEFAULT_FEATURE_ACCESS: Incomplete
EVENT_DESCRIPTION: str
EVENT_END_DATE: str
EVENT_END_DATETIME: str
EVENT_IN: str
EVENT_IN_DAYS: str
EVENT_IN_WEEKS: str
EVENT_START_DATE: str
EVENT_START_DATETIME: str
EVENT_SUMMARY: str
EVENT_TYPES_CONF: str
