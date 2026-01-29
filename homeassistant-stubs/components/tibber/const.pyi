from . import TibberRuntimeData as TibberRuntimeData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry

type TibberConfigEntry = ConfigEntry[TibberRuntimeData]
AUTH_IMPLEMENTATION: str
DATA_HASS_CONFIG: str
DOMAIN: str
MANUFACTURER: str
DATA_API_DEFAULT_SCOPES: Incomplete
