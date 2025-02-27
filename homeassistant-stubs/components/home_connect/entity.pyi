import abc
from .const import DOMAIN as DOMAIN
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectCoordinator as HomeConnectCoordinator
from .utils import get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from abc import abstractmethod
from aiohomeconnect.model import OptionKey
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete

class HomeConnectEntity(CoordinatorEntity[HomeConnectCoordinator], metaclass=abc.ABCMeta):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    appliance: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HomeConnectCoordinator, appliance: HomeConnectApplianceData, desc: EntityDescription) -> None: ...
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
