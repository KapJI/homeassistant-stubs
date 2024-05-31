import homeassistant.helpers.entity_registry as er
from .binary_sensor import BINARY_SENSORS as BINARY_SENSORS
from .const import CONF_CANDLE_LIGHT_MINUTES as CONF_CANDLE_LIGHT_MINUTES, CONF_DIASPORA as CONF_DIASPORA, CONF_HAVDALAH_OFFSET_MINUTES as CONF_HAVDALAH_OFFSET_MINUTES, DEFAULT_CANDLE_LIGHT as DEFAULT_CANDLE_LIGHT, DEFAULT_DIASPORA as DEFAULT_DIASPORA, DEFAULT_HAVDALAH_OFFSET_MINUTES as DEFAULT_HAVDALAH_OFFSET_MINUTES, DEFAULT_LANGUAGE as DEFAULT_LANGUAGE, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from .sensor import INFO_SENSORS as INFO_SENSORS, TIME_SENSORS as TIME_SENSORS
from _typeshed import Incomplete
from hdate import Location
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_ELEVATION as CONF_ELEVATION, CONF_LANGUAGE as CONF_LANGUAGE, CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, CONF_TIME_ZONE as CONF_TIME_ZONE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete

def get_unique_prefix(location: Location, language: str, candle_lighting_offset: int | None, havdalah_offset: int | None) -> str: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
def async_update_unique_ids(ent_reg: er.EntityRegistry, new_prefix: str, old_prefix: str) -> None: ...
