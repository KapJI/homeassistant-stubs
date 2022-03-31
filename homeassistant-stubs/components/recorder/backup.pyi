from . import Recorder as Recorder
from .const import DATA_INSTANCE as DATA_INSTANCE
from .util import async_migration_in_progress as async_migration_in_progress
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

_LOGGER: Any

async def async_pre_backup(hass: HomeAssistant) -> None: ...
async def async_post_backup(hass: HomeAssistant) -> None: ...
