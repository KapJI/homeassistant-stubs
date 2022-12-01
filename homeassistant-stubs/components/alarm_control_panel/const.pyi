from enum import IntFlag
from homeassistant.backports.enum import StrEnum as StrEnum
from typing import Final

DOMAIN: Final[str]
ATTR_CHANGED_BY: Final[str]
ATTR_CODE_ARM_REQUIRED: Final[str]

class CodeFormat(StrEnum):
    TEXT: str
    NUMBER: str

FORMAT_TEXT: Final[str]
FORMAT_NUMBER: Final[str]

class AlarmControlPanelEntityFeature(IntFlag):
    ARM_HOME: int
    ARM_AWAY: int
    ARM_NIGHT: int
    TRIGGER: int
    ARM_CUSTOM_BYPASS: int
    ARM_VACATION: int

SUPPORT_ALARM_ARM_HOME: Final[int]
SUPPORT_ALARM_ARM_AWAY: Final[int]
SUPPORT_ALARM_ARM_NIGHT: Final[int]
SUPPORT_ALARM_TRIGGER: Final[int]
SUPPORT_ALARM_ARM_CUSTOM_BYPASS: Final[int]
SUPPORT_ALARM_ARM_VACATION: Final[int]
CONDITION_TRIGGERED: Final[str]
CONDITION_DISARMED: Final[str]
CONDITION_ARMED_HOME: Final[str]
CONDITION_ARMED_AWAY: Final[str]
CONDITION_ARMED_NIGHT: Final[str]
CONDITION_ARMED_VACATION: Final[str]
CONDITION_ARMED_CUSTOM_BYPASS: Final[str]
