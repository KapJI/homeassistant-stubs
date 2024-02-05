from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from aiopulse import Roller as Roller
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

def async_add_acmeda_entities(hass: HomeAssistant, entity_class: type, config_entry: ConfigEntry, current: set[int], async_add_entities: AddEntitiesCallback) -> None: ...
async def update_devices(hass: HomeAssistant, config_entry: ConfigEntry, api: dict[int, Roller]) -> None: ...
