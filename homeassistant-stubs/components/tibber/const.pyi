from . import TibberRuntimeData as TibberRuntimeData
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN

type TibberConfigEntry = ConfigEntry[TibberRuntimeData]
CONF_LEGACY_ACCESS_TOKEN = CONF_ACCESS_TOKEN
AUTH_IMPLEMENTATION: str
DATA_HASS_CONFIG: str
DOMAIN: str
MANUFACTURER: str
DATA_API_DEFAULT_SCOPES: Incomplete
