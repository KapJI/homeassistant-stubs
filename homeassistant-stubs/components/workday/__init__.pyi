from .const import CONF_ADD_HOLIDAYS as CONF_ADD_HOLIDAYS, CONF_CATEGORY as CONF_CATEGORY, CONF_OFFSET as CONF_OFFSET, CONF_PROVINCE as CONF_PROVINCE, CONF_REMOVE_HOLIDAYS as CONF_REMOVE_HOLIDAYS, LOGGER as LOGGER, PLATFORMS as PLATFORMS
from .util import add_remove_custom_holidays as add_remove_custom_holidays, async_validate_country_and_province as async_validate_country_and_province, get_holidays_object as get_holidays_object, validate_dates as validate_dates
from holidays import HolidayBase
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_LANGUAGE as CONF_LANGUAGE
from homeassistant.core import HomeAssistant as HomeAssistant

type WorkdayConfigEntry = ConfigEntry[HolidayBase]
async def async_setup_entry(hass: HomeAssistant, entry: WorkdayConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WorkdayConfigEntry) -> bool: ...
