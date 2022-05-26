from _typeshed import Incomplete
from enum import Enum

DOMAIN: str
DEVICE_AUTH_IMPL: str
CONF_CALENDAR_ACCESS: str
DATA_CALENDARS: str
DATA_SERVICE: str
DATA_CONFIG: str
DISCOVER_CALENDAR: str

class FeatureAccess(Enum):
    read_only: str
    read_write: str
    _scope: Incomplete
    def __init__(self, scope: str) -> None: ...
    @property
    def scope(self) -> str: ...

DEFAULT_FEATURE_ACCESS: Incomplete
