import logging
from typing import override

class NoHeaderErrorFilter(logging.Filter):
    @override
    def filter(self, record: logging.LogRecord) -> bool: ...

def filter_urllib3_logging() -> None: ...
