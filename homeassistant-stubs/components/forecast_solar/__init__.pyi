from .const import CONF_DAMPING as CONF_DAMPING, CONF_DAMPING_EVENING as CONF_DAMPING_EVENING, CONF_DAMPING_MORNING as CONF_DAMPING_MORNING, CONF_MODULES_POWER as CONF_MODULES_POWER
from .coordinator import ForecastSolarConfigEntry as ForecastSolarConfigEntry, ForecastSolarDataUpdateCoordinator as ForecastSolarDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

async def async_migrate_entry(hass: HomeAssistant, entry: ForecastSolarConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ForecastSolarConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ForecastSolarConfigEntry) -> bool: ...
