from . import EnergyZeroDataUpdateCoordinator as EnergyZeroDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from .coordinator import EnergyZeroData as EnergyZeroData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

def get_gas_price(data: EnergyZeroData, hours: int) -> float | None: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
