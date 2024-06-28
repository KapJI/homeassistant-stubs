from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN
from .entity import OverkizEntity as OverkizEntity
from .water_heater_entities import CONTROLLABLE_NAME_TO_WATER_HEATER_ENTITY as CONTROLLABLE_NAME_TO_WATER_HEATER_ENTITY, WIDGET_TO_WATER_HEATER_ENTITY as WIDGET_TO_WATER_HEATER_ENTITY
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
