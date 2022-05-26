from _typeshed import Incomplete
from hdate import Location
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.typing import ConfigType as ConfigType

DOMAIN: str
PLATFORMS: list[Platform]
CONF_DIASPORA: str
CONF_LANGUAGE: str
CONF_CANDLE_LIGHT_MINUTES: str
CONF_HAVDALAH_OFFSET_MINUTES: str
CANDLE_LIGHT_DEFAULT: int
DEFAULT_NAME: str
CONFIG_SCHEMA: Incomplete

def get_unique_prefix(location: Location, language: str, candle_lighting_offset: Union[int, None], havdalah_offset: Union[int, None]) -> str: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
