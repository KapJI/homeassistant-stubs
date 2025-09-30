from . import WorkdayConfigEntry as WorkdayConfigEntry
from .const import CONF_EXCLUDES as CONF_EXCLUDES, CONF_OFFSET as CONF_OFFSET, CONF_WORKDAYS as CONF_WORKDAYS
from .entity import BaseWorkdayEntity as BaseWorkdayEntity
from _typeshed import Incomplete
from datetime import datetime
from holidays import HolidayBase as HolidayBase
from homeassistant.components.calendar import CalendarEntity as CalendarEntity, CalendarEvent as CalendarEvent
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: WorkdayConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WorkdayCalendarEntity(BaseWorkdayEntity, CalendarEntity):
    _attr_unique_id: Incomplete
    _attr_event: Incomplete
    event_list: list[CalendarEvent]
    _name: Incomplete
    def __init__(self, obj_holidays: HolidayBase, workdays: list[str], excludes: list[str], days_offset: int, name: str, entry_id: str) -> None: ...
    def update_data(self, now: datetime) -> None: ...
    @property
    def event(self) -> CalendarEvent | None: ...
    async def async_get_events(self, hass: HomeAssistant, start_date: datetime, end_date: datetime) -> list[CalendarEvent]: ...
