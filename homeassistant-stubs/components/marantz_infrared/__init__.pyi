from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

PLATFORMS: Incomplete

@dataclass
class MarantzIrRuntimeData:
    toggle: int = ...
type MarantzIrConfigEntry = ConfigEntry[MarantzIrRuntimeData]

async def async_setup_entry(hass: HomeAssistant, entry: MarantzIrConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MarantzIrConfigEntry) -> bool: ...
