import abc
from . import async_get_config_and_coordinator as async_get_config_and_coordinator, create_rest_data_from_config as create_rest_data_from_config
from .coordinator import RestCoordinator as RestCoordinator
from .data import RestData as RestData
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ICON as CONF_ICON, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.trigger_template_entity import CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_PICTURE as CONF_PICTURE
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import override

TRIGGER_ENTITY_OPTIONS: Incomplete
_LOGGER: Incomplete

async def async_get_config_rest_data_and_coordinator(hass: HomeAssistant, config: ConfigType, entity_domain: str, discovery_info: DiscoveryInfoType | None = None) -> tuple[ConfigType, RestData, RestCoordinator | None]: ...
def async_get_trigger_entity_config(hass: HomeAssistant, config: ConfigType, default_name: str) -> ConfigType: ...

class RestEntity(Entity, metaclass=abc.ABCMeta):
    _coordinator: Incomplete
    rest: Incomplete
    _resource_template: Incomplete
    _attr_should_poll: Incomplete
    _attr_force_update: Incomplete
    def __init__(self, coordinator: RestCoordinator | None, rest: RestData, resource_template: Template | None, force_update: bool) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_update(self) -> None: ...
    @abstractmethod
    def _update_from_rest_data(self) -> None: ...
