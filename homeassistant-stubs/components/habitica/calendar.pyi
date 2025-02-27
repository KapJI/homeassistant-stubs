import abc
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry, HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator
from .entity import HabiticaBase as HabiticaBase
from .util import build_rrule as build_rrule, get_recurrence_rule as get_recurrence_rule
from _typeshed import Incomplete
from abc import abstractmethod
from datetime import date, datetime
from dateutil.rrule import rrule as rrule
from enum import StrEnum
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEntityDescription as CalendarEntityDescription, CalendarEvent as CalendarEvent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

class HabiticaCalendar(StrEnum):
    DAILIES = 'dailys'
    TODOS = 'todos'
    TODO_REMINDERS = 'todo_reminders'
    DAILY_REMINDERS = 'daily_reminders'

async def async_setup_entry(hass: HomeAssistant, config_entry: HabiticaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HabiticaCalendarEntity(HabiticaBase, CalendarEntity, metaclass=abc.ABCMeta):
    def __init__(self, coordinator: HabiticaDataUpdateCoordinator) -> None: ...
    @abstractmethod
    def get_events(self, start_date: datetime, end_date: datetime | None = None) -> list[CalendarEvent]: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
    @property
    def start_of_today(self) -> datetime: ...
    def get_recurrence_dates(self, recurrences: rrule, start_date: datetime, end_date: datetime | None = None) -> list[datetime]: ...

class HabiticaTodosCalendarEntity(HabiticaCalendarEntity):
    entity_description: Incomplete
    def get_events(self, start_date: datetime, end_date: datetime | None = None) -> list[CalendarEvent]: ...

class HabiticaDailiesCalendarEntity(HabiticaCalendarEntity):
    entity_description: Incomplete
    def end_date(self, recurrence: datetime, end: datetime | None = None) -> date: ...
    def get_events(self, start_date: datetime, end_date: datetime | None = None) -> list[CalendarEvent]: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool | None] | None: ...

class HabiticaTodoRemindersCalendarEntity(HabiticaCalendarEntity):
    entity_description: Incomplete
    def get_events(self, start_date: datetime, end_date: datetime | None = None) -> list[CalendarEvent]: ...

class HabiticaDailyRemindersCalendarEntity(HabiticaCalendarEntity):
    entity_description: Incomplete
    def start(self, reminder_time: datetime, reminder_date: date) -> datetime: ...
    def get_events(self, start_date: datetime, end_date: datetime | None = None) -> list[CalendarEvent]: ...
