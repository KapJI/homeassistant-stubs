from _typeshed import Incomplete
from enum import IntFlag, StrEnum
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from typing import Final

DOMAIN: Final[str]
ATTR_CHANGED_BY: Final[str]
ATTR_CODE_ARM_REQUIRED: Final[str]

class CodeFormat(StrEnum):
    TEXT: str
    NUMBER: str

_DEPRECATED_FORMAT_TEXT: Final[Incomplete]
_DEPRECATED_FORMAT_NUMBER: Final[Incomplete]

class AlarmControlPanelEntityFeature(IntFlag):
    ARM_HOME: int
    ARM_AWAY: int
    ARM_NIGHT: int
    TRIGGER: int
    ARM_CUSTOM_BYPASS: int
    ARM_VACATION: int

_DEPRECATED_SUPPORT_ALARM_ARM_HOME: Final[Incomplete]
_DEPRECATED_SUPPORT_ALARM_ARM_AWAY: Final[Incomplete]
_DEPRECATED_SUPPORT_ALARM_ARM_NIGHT: Final[Incomplete]
_DEPRECATED_SUPPORT_ALARM_TRIGGER: Final[Incomplete]
_DEPRECATED_SUPPORT_ALARM_ARM_CUSTOM_BYPASS: Final[Incomplete]
_DEPRECATED_SUPPORT_ALARM_ARM_VACATION: Final[Incomplete]
CONDITION_TRIGGERED: Final[str]
CONDITION_DISARMED: Final[str]
CONDITION_ARMED_HOME: Final[str]
CONDITION_ARMED_AWAY: Final[str]
CONDITION_ARMED_NIGHT: Final[str]
CONDITION_ARMED_VACATION: Final[str]
CONDITION_ARMED_CUSTOM_BYPASS: Final[str]
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
