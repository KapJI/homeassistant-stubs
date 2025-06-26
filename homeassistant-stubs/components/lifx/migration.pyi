from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .coordinator import LIFXConfigEntry as LIFXConfigEntry
from .discovery import async_init_discovery_flow as async_init_discovery_flow
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_migrate_legacy_entries(hass: HomeAssistant, discovered_hosts_by_serial: dict[str, str], existing_serials: set[str], legacy_entry: LIFXConfigEntry) -> int: ...
@callback
def async_migrate_entities_devices(hass: HomeAssistant, legacy_entry_id: str, new_entry: LIFXConfigEntry) -> None: ...
