from ..const import SupportedDialect as SupportedDialect
from awesomeversion import AwesomeVersion as AwesomeVersion

class UnsupportedDialect(Exception): ...

class DatabaseEngine:
    dialect: SupportedDialect
    optimizer: DatabaseOptimizer
    version: AwesomeVersion | None
    def __init__(self, dialect, optimizer, version) -> None: ...

class DatabaseOptimizer:
    slow_range_in_select: bool
    def __init__(self, slow_range_in_select) -> None: ...
