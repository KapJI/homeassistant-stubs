from .core import Context as Context
from _typeshed import Incomplete
from collections.abc import Generator, Sequence
from dataclasses import dataclass

class HomeAssistantError(Exception):
    translation_domain: Incomplete
    translation_key: Incomplete
    translation_placeholders: Incomplete
    def __init__(self, *args: object, translation_domain: str | None = None, translation_key: str | None = None, translation_placeholders: dict[str, str] | None = None) -> None: ...

class ConfigValidationError(HomeAssistantError, ExceptionGroup[Exception]):
    _message: Incomplete
    def __init__(self, message: str, exceptions: list[Exception], translation_domain: str | None = None, translation_key: str | None = None, translation_placeholders: dict[str, str] | None = None) -> None: ...
    def __str__(self) -> str: ...

class ServiceValidationError(HomeAssistantError): ...
class InvalidEntityFormatError(HomeAssistantError): ...
class NoEntitySpecifiedError(HomeAssistantError): ...

class TemplateError(HomeAssistantError):
    def __init__(self, exception: Exception | str) -> None: ...

@dataclass(slots=True)
class ConditionError(HomeAssistantError):
    type: str
    @staticmethod
    def _indent(indent: int, message: str) -> str: ...
    def output(self, indent: int) -> Generator[str, None, None]: ...
    def __str__(self) -> str: ...
    def __init__(self, type) -> None: ...

@dataclass(slots=True)
class ConditionErrorMessage(ConditionError):
    message: str
    def output(self, indent: int) -> Generator[str, None, None]: ...
    def __init__(self, type, message) -> None: ...

@dataclass(slots=True)
class ConditionErrorIndex(ConditionError):
    index: int
    total: int
    error: ConditionError
    def output(self, indent: int) -> Generator[str, None, None]: ...
    def __init__(self, type, index, total, error) -> None: ...

@dataclass(slots=True)
class ConditionErrorContainer(ConditionError):
    errors: Sequence[ConditionError]
    def output(self, indent: int) -> Generator[str, None, None]: ...
    def __init__(self, type, errors) -> None: ...

class IntegrationError(HomeAssistantError):
    def __str__(self) -> str: ...

class PlatformNotReady(IntegrationError): ...
class ConfigEntryError(IntegrationError): ...
class ConfigEntryNotReady(IntegrationError): ...
class ConfigEntryAuthFailed(IntegrationError): ...
class InvalidStateError(HomeAssistantError): ...

class Unauthorized(HomeAssistantError):
    context: Incomplete
    user_id: Incomplete
    entity_id: Incomplete
    config_entry_id: Incomplete
    perm_category: Incomplete
    permission: Incomplete
    def __init__(self, context: Context | None = None, user_id: str | None = None, entity_id: str | None = None, config_entry_id: str | None = None, perm_category: str | None = None, permission: str | None = None) -> None: ...

class UnknownUser(Unauthorized): ...

class ServiceNotFound(HomeAssistantError):
    domain: Incomplete
    service: Incomplete
    def __init__(self, domain: str, service: str) -> None: ...
    def __str__(self) -> str: ...

class MaxLengthExceeded(HomeAssistantError):
    value: Incomplete
    property_name: Incomplete
    max_length: Incomplete
    def __init__(self, value: str, property_name: str, max_length: int) -> None: ...

class DependencyError(HomeAssistantError):
    failed_dependencies: Incomplete
    def __init__(self, failed_dependencies: list[str]) -> None: ...
