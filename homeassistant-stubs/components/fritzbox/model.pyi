from collections.abc import Callable as Callable
from pyfritzhome import FritzhomeDevice as FritzhomeDevice
from typing import TypedDict

class ClimateExtraAttributes(TypedDict, total=False):
    battery_level: int
    battery_low: bool
    holiday_mode: bool
    summer_mode: bool
    window_open: bool

class FritzEntityDescriptionMixinBase:
    suitable: Callable[[FritzhomeDevice], bool]
    def __init__(self, suitable) -> None: ...
