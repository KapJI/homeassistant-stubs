from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
ATTR_DISTANCE: str
ATTR_SOURCE: str
DOMAIN: str
ENTITY_ID_FORMAT: Incomplete
SCAN_INTERVAL: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class GeolocationEvent(Entity):
    _attr_source: str
    _attr_distance: Union[float, None]
    _attr_latitude: Union[float, None]
    _attr_longitude: Union[float, None]
    @property
    def state(self) -> Union[float, None]: ...
    @property
    def source(self) -> str: ...
    @property
    def distance(self) -> Union[float, None]: ...
    @property
    def latitude(self) -> Union[float, None]: ...
    @property
    def longitude(self) -> Union[float, None]: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
