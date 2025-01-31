from .. import DeconzConfigEntry as DeconzConfigEntry
from ..const import LOGGER as LOGGER
from ..errors import AuthenticationRequired as AuthenticationRequired, CannotConnect as CannotConnect
from .config import DeconzConfig as DeconzConfig
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import aiohttp_client as aiohttp_client
from pydeconz import DeconzSession

async def get_deconz_api(hass: HomeAssistant, config_entry: DeconzConfigEntry) -> DeconzSession: ...
