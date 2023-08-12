from .entity import HomeWizardEntity as HomeWizardEntity
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate, ParamSpec, TypeVar

_HomeWizardEntityT = TypeVar('_HomeWizardEntityT', bound=HomeWizardEntity)
_P = ParamSpec('_P')

def homewizard_exception_handler(func: Callable[Concatenate[_HomeWizardEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_HomeWizardEntityT, _P], Coroutine[Any, Any, None]]: ...
