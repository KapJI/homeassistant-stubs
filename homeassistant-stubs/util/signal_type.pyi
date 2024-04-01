from dataclasses import dataclass
from typing import Any, Generic, TypeVarTuple

_Ts = TypeVarTuple('_Ts')

@dataclass(frozen=True)
class _SignalTypeBase(Generic[*_Ts]):
    name: str
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __init__(self, name) -> None: ...

@dataclass(frozen=True, eq=False)
class SignalType(_SignalTypeBase[*_Ts]):
    def __init__(self, name) -> None: ...

@dataclass(frozen=True, eq=False)
class SignalTypeFormat(_SignalTypeBase[*_Ts]):
    def format(self, *args: Any, **kwargs: Any) -> SignalType[Unpack[_Ts]]: ...
    def __init__(self, name) -> None: ...
