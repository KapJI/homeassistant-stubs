from .const import CONF_ZIP_CODE as CONF_ZIP_CODE, TYPE_ALLERGY_FORECAST as TYPE_ALLERGY_FORECAST, TYPE_ALLERGY_INDEX as TYPE_ALLERGY_INDEX, TYPE_ALLERGY_OUTLOOK as TYPE_ALLERGY_OUTLOOK, TYPE_ASTHMA_FORECAST as TYPE_ASTHMA_FORECAST, TYPE_ASTHMA_INDEX as TYPE_ASTHMA_INDEX, TYPE_DISEASE_FORECAST as TYPE_DISEASE_FORECAST, TYPE_DISEASE_INDEX as TYPE_DISEASE_INDEX
from .coordinator import IqviaConfigEntry as IqviaConfigEntry, IqviaUpdateCoordinator as IqviaUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client

DEFAULT_ATTRIBUTION: str
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IqviaConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: IqviaConfigEntry) -> bool: ...
