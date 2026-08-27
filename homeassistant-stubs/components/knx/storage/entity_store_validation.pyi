import probatio
from .entity_store_schema import ENTITY_STORE_DATA_SCHEMA as ENTITY_STORE_DATA_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from typing import Any, Literal, TypedDict

class _ErrorDescription(TypedDict):
    path: list[str]
    message: str
    code: str | None
    translation_key: str | None
    placeholders: dict[str, Any]
    context: dict[str, Any]
    secret: bool

class EntityStoreValidationError(TypedDict):
    success: Literal[False]
    error_base: str
    errors: list[_ErrorDescription]

class EntityStoreValidationSuccess(TypedDict):
    success: Literal[True]
    entity_id: str | None

def parse_invalid(exc: probatio.Invalid) -> _ErrorDescription: ...
def validate_config_store_data(schema: Callable[[dict], dict], entity_data: dict) -> dict: ...
def validate_entity_data(entity_data: dict) -> dict: ...

class EntityStoreValidationException(Exception):
    validation_error: Incomplete
    def __init__(self, validation_error: EntityStoreValidationError) -> None: ...
