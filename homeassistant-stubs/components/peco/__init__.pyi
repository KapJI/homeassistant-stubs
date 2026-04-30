from .const import CONF_PHONE_NUMBER as CONF_PHONE_NUMBER
from .coordinator import PecoConfigEntry as PecoConfigEntry, PecoOutageCoordinator as PecoOutageCoordinator, PecoRuntimeData as PecoRuntimeData, PecoSmartMeterCoordinator as PecoSmartMeterCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Final

PLATFORMS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: PecoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: PecoConfigEntry) -> bool: ...
