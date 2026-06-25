from _typeshed import Incomplete
from enum import StrEnum

CONF_TRIGGER_VARIABLES: str
DOMAIN: str

class AutomationEntityCapabilityAttribute(StrEnum):
    ID = 'id'

class AutomationEntityStateAttribute(StrEnum):
    LAST_TRIGGERED = 'last_triggered'
    MODE = 'mode'
    CUR = 'current'
    MAX = 'max'

CONF_HIDE_ENTITY: str
CONF_CONDITION_TYPE: str
CONF_INITIAL_STATE: str
CONF_BLUEPRINT: str
CONF_INPUT: str
CONF_TRACE: str
DEFAULT_INITIAL_STATE: bool
LOGGER: Incomplete
