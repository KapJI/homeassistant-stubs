from .const import CONF_COUNTER_ID as CONF_COUNTER_ID
from .coordinator import SuezWaterConfigEntry as SuezWaterConfigEntry, SuezWaterCoordinator as SuezWaterCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: list[Platform]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SuezWaterConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SuezWaterConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: SuezWaterConfigEntry) -> bool: ...
