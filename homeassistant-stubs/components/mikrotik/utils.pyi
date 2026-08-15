from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .errors import CannotConnect as CannotConnect, LoginError as LoginError
from collections.abc import Generator
from contextlib import contextmanager
from datetime import datetime
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.update_coordinator import UpdateFailed as UpdateFailed
from homeassistant.util.dt import utcnow as utcnow

def percentage(total: float, free: float) -> float | None: ...
def calculate_uptime(uptime_string: str) -> datetime | None: ...
@contextmanager
def mikrotik_config_entry_errors(suppress_errors: bool = False, during_setup: bool = False) -> Generator[None]: ...
