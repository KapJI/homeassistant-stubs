from enum import IntEnum

CONF_EVENT: str

class CalendarEntityFeature(IntEnum):
    CREATE_EVENT: int
    DELETE_EVENT: int

EVENT_UID: str
EVENT_START: str
EVENT_END: str
EVENT_SUMMARY: str
EVENT_DESCRIPTION: str
EVENT_LOCATION: str
EVENT_RECURRENCE_ID: str
EVENT_RECURRENCE_RANGE: str
EVENT_RRULE: str
