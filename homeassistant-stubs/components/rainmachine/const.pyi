from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum

LOGGER: Incomplete
DOMAIN: str
CONF_ZONE_RUN_TIME: str
DATA_CONTROLLER: str
DATA_COORDINATOR: str
DATA_PROGRAMS: str
DATA_PROVISION_SETTINGS: str
DATA_RESTRICTIONS_CURRENT: str
DATA_RESTRICTIONS_UNIVERSAL: str
DATA_ZONES: str
DEFAULT_PORT: int
DEFAULT_ZONE_RUN: Incomplete

class RunStates(StrEnum):
    NOT_RUNNING: str
    QUEUED: str
    RUNNING: str

RUN_STATE_MAP: Incomplete
