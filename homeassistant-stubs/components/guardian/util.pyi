from . import GuardianEntity as GuardianEntity
from .const import LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine, Iterable
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate, ParamSpec, TypeVar

_GuardianEntityT = TypeVar('_GuardianEntityT', bound=GuardianEntity)
DEFAULT_UPDATE_INTERVAL: Incomplete
SIGNAL_REBOOT_REQUESTED: str
_P = ParamSpec('_P')

@dataclass
class EntityDomainReplacementStrategy:
    old_domain: str
    old_unique_id: str
    def __init__(self, old_domain, old_unique_id) -> None: ...

def async_finish_entity_domain_replacements(hass: HomeAssistant, entry: ConfigEntry, entity_replacement_strategies: Iterable[EntityDomainReplacementStrategy]) -> None: ...
def convert_exceptions_to_homeassistant_error(func: Callable[Concatenate[_GuardianEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_GuardianEntityT, _P], Coroutine[Any, Any, None]]: ...
