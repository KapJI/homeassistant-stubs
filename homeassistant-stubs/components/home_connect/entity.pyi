import abc
from .const import API_DEFAULT_RETRY_AFTER as API_DEFAULT_RETRY_AFTER, DOMAIN as DOMAIN
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectCoordinator as HomeConnectCoordinator
from .utils import get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from abc import abstractmethod
from aiohomeconnect.model import OptionKey
from collections.abc import Callable as Callable, Coroutine
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Concatenate

_LOGGER: Incomplete

class HomeConnectEntity(CoordinatorEntity[HomeConnectCoordinator], metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    appliance: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HomeConnectCoordinator, appliance: HomeConnectApplianceData, desc: EntityDescription, context_override: Any | None = None) -> None: ...
    @abstractmethod
    def update_native_value(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def bsh_key(self) -> str: ...
    @property
    def available(self) -> bool: ...

class HomeConnectOptionEntity(HomeConnectEntity, metaclass=abc.ABCMeta):
    @property
    def available(self) -> bool: ...
    @property
    def option_value(self) -> str | int | float | bool | None: ...
    async def async_set_option(self, value: str | float | bool) -> None: ...
    @property
    def bsh_key(self) -> OptionKey: ...

def constraint_fetcher[_EntityT: HomeConnectEntity, **_P](func: Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, None]]: ...
