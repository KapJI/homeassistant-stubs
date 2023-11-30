from _typeshed import Incomplete
from enum import Enum, StrEnum

DOMAIN: str
CONF_CALENDAR_ACCESS: str
CONF_CREDENTIAL_TYPE: str
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

class CredentialType(StrEnum):
    DEVICE_AUTH: str
    WEB_AUTH: str

EVENT_DESCRIPTION: str
EVENT_END_DATE: str
EVENT_END_DATETIME: str
EVENT_IN: str
EVENT_IN_DAYS: str
EVENT_IN_WEEKS: str
EVENT_LOCATION: str
EVENT_START_DATE: str
EVENT_START_DATETIME: str
EVENT_SUMMARY: str
EVENT_TYPES_CONF: str
