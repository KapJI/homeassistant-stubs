from . import singleton as singleton, storage as storage
from homeassistant.core import HomeAssistant as HomeAssistant

DATA_KEY: str
DATA_VERSION: int
LEGACY_UUID_FILE: str

async def async_get(hass: HomeAssistant) -> str: ...
