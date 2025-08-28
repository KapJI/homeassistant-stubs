import abc
from . import SleepAsAndroidConfigEntry as SleepAsAndroidConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.const import CONF_WEBHOOK_ID as CONF_WEBHOOK_ID
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription

class SleepAsAndroidEntity(Entity, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    webhook_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry: SleepAsAndroidConfigEntry, entity_description: EntityDescription) -> None: ...
    @abstractmethod
    def _async_handle_event(self, webhook_id: str, data: dict[str, str]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
