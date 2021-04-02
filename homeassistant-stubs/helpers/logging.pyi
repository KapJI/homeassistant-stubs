import logging
from typing import Any, Mapping, MutableMapping

class KeywordMessage:
    _fmt: Any = ...
    _args: Any = ...
    _kwargs: Any = ...
    def __init__(self, fmt: Any, args: Any, kwargs: Mapping[str, Any]) -> None: ...
    def __str__(self) -> str: ...

class KeywordStyleAdapter(logging.LoggerAdapter):
    def __init__(self, logger: logging.Logger, extra: Union[Mapping[str, Any], None]=...) -> None: ...
    def log(self, level: int, msg: Any, *args: Any, **kwargs: Any) -> None: ...
    def process(self, msg: Any, kwargs: MutableMapping[str, Any]) -> tuple[Any, MutableMapping[str, Any]]: ...
