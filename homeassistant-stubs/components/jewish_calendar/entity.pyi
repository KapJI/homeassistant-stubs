import abc
import datetime as dt
from .const import DOMAIN as DOMAIN
from .coordinator import JewishCalendarConfigEntry as JewishCalendarConfigEntry, JewishCalendarUpdateCoordinator as JewishCalendarUpdateCoordinator
from _typeshed import Incomplete
from abc import abstractmethod
from hdate import Zmanim as Zmanim
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class JewishCalendarEntity(CoordinatorEntity[JewishCalendarUpdateCoordinator], metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _update_unsub: CALLBACK_TYPE | None
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, config_entry: JewishCalendarConfigEntry, description: EntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @abstractmethod
    def _update_times(self, zmanim: Zmanim) -> list[dt.datetime | None]: ...
    def _schedule_update(self) -> None: ...
    @callback
    def _update(self, now: dt.datetime | None = None) -> None: ...
