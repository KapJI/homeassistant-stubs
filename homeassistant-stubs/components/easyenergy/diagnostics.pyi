from . import EasyEnergyDataUpdateCoordinator as EasyEnergyDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from .coordinator import EasyEnergyData as EasyEnergyData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

def get_gas_price(data: EasyEnergyData, hours: int) -> float | None: ...
async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
