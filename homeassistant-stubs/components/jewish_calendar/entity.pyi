import abc
import datetime as dt
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from dataclasses import dataclass
from hdate import HDateInfo, Location as Location, Zmanim
from hdate.translator import Language as Language
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription

_LOGGER: Incomplete
type JewishCalendarConfigEntry = ConfigEntry[JewishCalendarData]

@dataclass
class JewishCalendarDataResults:
    dateinfo: HDateInfo
    zmanim: Zmanim

@dataclass
class JewishCalendarData:
    language: Language
    diaspora: bool
    location: Location
    candle_lighting_offset: int
    havdalah_offset: int
    results: JewishCalendarDataResults | None = ...

class JewishCalendarEntity(Entity, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _update_unsub: CALLBACK_TYPE | None
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    data: Incomplete
    def __init__(self, config_entry: JewishCalendarConfigEntry, description: EntityDescription) -> None: ...
    def make_zmanim(self, date: dt.date) -> Zmanim: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @abstractmethod
    def _update_times(self, zmanim: Zmanim) -> list[dt.datetime | None]: ...
    def _schedule_update(self) -> None: ...
    @callback
    def _update(self, now: dt.datetime | None = None) -> None: ...
    def create_results(self, now: dt.datetime | None = None) -> None: ...
