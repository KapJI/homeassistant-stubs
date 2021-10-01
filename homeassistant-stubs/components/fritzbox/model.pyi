from collections.abc import Callable as Callable
from pyfritzhome import FritzhomeDevice as FritzhomeDevice
from typing import TypedDict

class FritzExtraAttributes(TypedDict):
    device_locked: bool
    locked: bool

class ClimateExtraAttributes(FritzExtraAttributes):
    battery_low: bool
    battery_level: int
    holiday_mode: bool
    summer_mode: bool
    window_open: bool

class FritzEntityDescriptionMixinBase:
    suitable: Callable[[FritzhomeDevice], bool]
