import abc
from .const import ALLOWED_DAYS as ALLOWED_DAYS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from abc import abstractmethod
from datetime import date, datetime
from holidays import HolidayBase as HolidayBase
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, ServiceResponse as ServiceResponse, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time

class BaseWorkdayEntity(Entity, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _attr_translation_key = DOMAIN
    _attr_should_poll: bool
    unsub: CALLBACK_TYPE | None
    _obj_holidays: Incomplete
    _workdays: Incomplete
    _excludes: Incomplete
    _days_offset: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, obj_holidays: HolidayBase, workdays: list[str], excludes: list[str], days_offset: int, name: str, entry_id: str) -> None: ...
    def is_include(self, day: str, now: date) -> bool: ...
    def is_exclude(self, day: str, now: date) -> bool: ...
    def get_next_interval(self, now: datetime) -> datetime: ...
    def _update_state_and_setup_listener(self) -> None: ...
    @callback
    def point_in_time_listener(self, time_date: datetime) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @abstractmethod
    def update_data(self, now: datetime) -> None: ...
    def check_date(self, check_date: date) -> ServiceResponse: ...
    def date_is_workday(self, check_date: date) -> bool: ...
