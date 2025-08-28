from . import WorkdayConfigEntry as WorkdayConfigEntry
from .const import CONF_REMOVE_HOLIDAYS as CONF_REMOVE_HOLIDAYS, DOMAIN as DOMAIN, LOGGER as LOGGER
from holidays import DateLike as DateLike, HolidayBase
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.setup import SetupPhases as SetupPhases, async_pause_setup as async_pause_setup
from homeassistant.util import slugify as slugify

async def async_validate_country_and_province(hass: HomeAssistant, entry: WorkdayConfigEntry, country: str | None, province: str | None) -> None: ...
def validate_dates(holiday_list: list[str]) -> list[str]: ...
def get_holidays_object(country: str | None, province: str | None, year: int, language: str | None, categories: list[str] | None) -> HolidayBase: ...
def add_remove_custom_holidays(hass: HomeAssistant, entry: WorkdayConfigEntry, country: str | None, calc_add_holidays: list[DateLike], calc_remove_holidays: list[str]) -> None: ...
