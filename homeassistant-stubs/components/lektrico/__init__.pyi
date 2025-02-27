from .coordinator import LektricoConfigEntry as LektricoConfigEntry, LektricoDeviceDataUpdateCoordinator as LektricoDeviceDataUpdateCoordinator
from homeassistant.const import CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

CHARGERS_PLATFORMS: list[Platform]
LB_DEVICES_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: LektricoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LektricoConfigEntry) -> bool: ...
def _get_platforms(entry: LektricoConfigEntry) -> list[Platform]: ...
