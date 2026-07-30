from .const import DOMAIN as DOMAIN
from .errors import CannotConnect as CannotConnect, LoginError as LoginError
from collections.abc import Generator
from contextlib import contextmanager
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.update_coordinator import UpdateFailed as UpdateFailed

@contextmanager
def mikrotik_config_entry_errors(suppress_errors: bool = False, during_setup: bool = False) -> Generator[None]: ...
