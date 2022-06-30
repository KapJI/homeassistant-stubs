from .const import DOMAIN as DOMAIN, ISY994_ISY as ISY994_ISY, ISY994_NODES as ISY994_NODES, ISY994_PROGRAMS as ISY994_PROGRAMS, ISY994_VARIABLES as ISY994_VARIABLES, PLATFORMS as PLATFORMS, PROGRAM_PLATFORMS as PROGRAM_PLATFORMS
from homeassistant.core import HomeAssistant as HomeAssistant

def unique_ids_for_config_entry_id(hass: HomeAssistant, config_entry_id: str) -> set[str]: ...
