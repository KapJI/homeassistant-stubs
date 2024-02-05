from _typeshed import Incomplete
from enum import IntFlag
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from typing import Final

DOMAIN: Final[str]
ATTR_TONE: Final[str]
ATTR_AVAILABLE_TONES: Final[str]
ATTR_DURATION: Final[str]
ATTR_VOLUME_LEVEL: Final[str]

class SirenEntityFeature(IntFlag):
    TURN_ON: int
    TURN_OFF: int
    TONES: int
    VOLUME_SET: int
    DURATION: int

_DEPRECATED_SUPPORT_TURN_ON: Final[Incomplete]
_DEPRECATED_SUPPORT_TURN_OFF: Final[Incomplete]
_DEPRECATED_SUPPORT_TONES: Final[Incomplete]
_DEPRECATED_SUPPORT_VOLUME_SET: Final[Incomplete]
_DEPRECATED_SUPPORT_DURATION: Final[Incomplete]
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
