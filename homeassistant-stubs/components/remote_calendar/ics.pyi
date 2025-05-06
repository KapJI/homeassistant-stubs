from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from ical.calendar import Calendar as Calendar

_LOGGER: Incomplete

class InvalidIcsException(Exception): ...

def _compat_calendar_from_ics(ics: str) -> Calendar: ...
async def parse_calendar(hass: HomeAssistant, ics: str) -> Calendar: ...
