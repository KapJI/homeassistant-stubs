from _typeshed import Incomplete
from enum import StrEnum
from typing import Final

DOMAIN: Final[str]
LOGGER: Incomplete

class ScheduleEntityCapabilityAttribute(StrEnum):
    EDITABLE = 'editable'

class ScheduleEntityStateAttribute(StrEnum):
    NEXT_EVENT = 'next_event'

CONF_DATA: Final[str]
CONF_FRIDAY: Final[str]
CONF_FROM: Final[str]
CONF_MONDAY: Final[str]
CONF_SATURDAY: Final[str]
CONF_SUNDAY: Final[str]
CONF_THURSDAY: Final[str]
CONF_TO: Final[str]
CONF_TUESDAY: Final[str]
CONF_WEDNESDAY: Final[str]
CONF_ALL_DAYS: Final[Incomplete]
ATTR_NEXT_EVENT: Final[str]
WEEKDAY_TO_CONF: Final[Incomplete]
SERVICE_GET: Final[str]
