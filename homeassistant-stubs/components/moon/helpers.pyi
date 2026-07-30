from homeassistant.core import callback as callback

STATE_FIRST_QUARTER: str
STATE_FULL_MOON: str
STATE_LAST_QUARTER: str
STATE_NEW_MOON: str
STATE_WANING_CRESCENT: str
STATE_WANING_GIBBOUS: str
STATE_WAXING_CRESCENT: str
STATE_WAXING_GIBBOUS: str
MOON_PHASES: tuple[str, ...]
_FULL_MOON_PHASE_VALUE: int

@callback
def moon_phase() -> str: ...
@callback
def is_waxing() -> bool: ...
