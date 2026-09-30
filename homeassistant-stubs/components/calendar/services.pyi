import datetime
from . import CalendarEntity as CalendarEntity
from .const import CREATE_EVENT_SERVICE as CREATE_EVENT_SERVICE, CalendarEntityFeature as CalendarEntityFeature, DATA_COMPONENT as DATA_COMPONENT, EVENT_DESCRIPTION as EVENT_DESCRIPTION, EVENT_DURATION as EVENT_DURATION, EVENT_END as EVENT_END, EVENT_END_DATE as EVENT_END_DATE, EVENT_END_DATETIME as EVENT_END_DATETIME, EVENT_IN as EVENT_IN, EVENT_IN_DAYS as EVENT_IN_DAYS, EVENT_IN_WEEKS as EVENT_IN_WEEKS, EVENT_LOCATION as EVENT_LOCATION, EVENT_START as EVENT_START, EVENT_START_DATE as EVENT_START_DATE, EVENT_START_DATETIME as EVENT_START_DATETIME, EVENT_SUMMARY as EVENT_SUMMARY, EVENT_TIME_FIELDS as EVENT_TIME_FIELDS, EVENT_TYPES as EVENT_TYPES, SERVICE_GET_EVENTS as SERVICE_GET_EVENTS
from .helper import MIN_NEW_EVENT_DURATION as MIN_NEW_EVENT_DURATION, as_local_timezone as as_local_timezone, has_consistent_timezone as has_consistent_timezone, has_min_duration as has_min_duration, has_positive_interval as has_positive_interval, list_events_dict_factory as list_events_dict_factory
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from typing import Any, Final

CREATE_EVENT_SCHEMA: Incomplete
SERVICE_GET_EVENTS_SCHEMA: Final[Incomplete]

def _validate_timespan(values: dict[str, Any]) -> tuple[datetime.datetime | datetime.date, datetime.datetime | datetime.date]: ...
async def async_create_event(entity: CalendarEntity, call: ServiceCall) -> None: ...
async def async_get_events_service(calendar: CalendarEntity, service_call: ServiceCall) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
