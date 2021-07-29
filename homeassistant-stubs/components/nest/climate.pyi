from .climate_sdm import async_setup_sdm_entry as async_setup_sdm_entry
from .const import DATA_SDM as DATA_SDM
from .legacy.climate import async_setup_legacy_entry as async_setup_legacy_entry
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
