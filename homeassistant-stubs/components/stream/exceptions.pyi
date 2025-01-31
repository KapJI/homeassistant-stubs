from .const import StreamClientError as StreamClientError
from _typeshed import Incomplete
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

class StreamOpenClientError(HomeAssistantError):
    error_code: Incomplete
    def __init__(self, message: str, error_code: StreamClientError) -> None: ...

class StreamWorkerError(Exception):
    error_code: Incomplete
    def __init__(self, message: str, error_code: StreamClientError = ...) -> None: ...

class StreamEndedError(StreamWorkerError): ...
