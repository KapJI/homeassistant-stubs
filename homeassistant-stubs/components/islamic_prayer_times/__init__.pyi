from .coordinator import IslamicPrayerDataUpdateCoordinator as IslamicPrayerDataUpdateCoordinator, IslamicPrayerTimesConfigEntry as IslamicPrayerTimesConfigEntry
from _typeshed import Incomplete
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

PLATFORMS: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: IslamicPrayerTimesConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: IslamicPrayerTimesConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: IslamicPrayerTimesConfigEntry) -> bool: ...
async def async_options_updated(hass: HomeAssistant, entry: IslamicPrayerTimesConfigEntry) -> None: ...
