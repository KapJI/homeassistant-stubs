from collections.abc import Callable as Callable, Hashable as Hashable

class Registry(dict[_KT, _VT]):
    def register(self, name: _KT) -> Callable[[_VT], _VT]: ...
