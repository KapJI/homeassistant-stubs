from .coordinator import FireflyConfigEntry as FireflyConfigEntry, FireflyDataUpdateCoordinator as FireflyDataUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: FireflyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FireflyConfigEntry) -> bool: ...
