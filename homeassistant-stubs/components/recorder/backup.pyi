from . import Recorder as Recorder
from .const import DATA_INSTANCE as DATA_INSTANCE
from .util import async_migration_in_progress as async_migration_in_progress
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

_LOGGER: Incomplete

async def async_pre_backup(hass: HomeAssistant) -> None: ...
async def async_post_backup(hass: HomeAssistant) -> None: ...
