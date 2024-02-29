from _typeshed import Incomplete
from collections.abc import Callable as Callable
from typing import Any
from xknx.dpt import DPTBase

def dpt_subclass_validator(dpt_base_class: type[DPTBase]) -> Callable[[Any], str | int]: ...

numeric_type_validator: Incomplete
sensor_type_validator: Incomplete
string_type_validator: Incomplete

def ga_validator(value: Any) -> str | int: ...

ga_list_validator: Incomplete
ia_validator: Incomplete

def ip_v4_validator(value: Any, multicast: bool | None = None) -> str: ...

sync_state_validator: Incomplete
