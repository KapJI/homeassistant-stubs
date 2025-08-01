from .const import CONF_PROVINCE as CONF_PROVINCE, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from holidays import HolidayBase as HolidayBase
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, CONF_LANGUAGE as CONF_LANGUAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.setup import SetupPhases as SetupPhases, async_pause_setup as async_pause_setup

async def _async_validate_country_and_province(hass: HomeAssistant, entry: ConfigEntry, country: str | None, province: str | None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
