from .coordinator import NamecheapConfigEntry as NamecheapConfigEntry, NamecheapDnsUpdateCoordinator as NamecheapDnsUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: NamecheapConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: NamecheapConfigEntry) -> bool: ...
