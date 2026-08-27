from .const import DOMAIN as DOMAIN
from collections.abc import Iterator
from contextlib import contextmanager
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from typing import Any

@contextmanager
def openevse_exception_handler(value: Any = None) -> Iterator[None]: ...
