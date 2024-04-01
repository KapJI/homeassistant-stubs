from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .climate_entities import Controllable as Controllable, WIDGET_AND_CONTROLLABLE_TO_CLIMATE_ENTITY as WIDGET_AND_CONTROLLABLE_TO_CLIMATE_ENTITY, WIDGET_AND_PROTOCOL_TO_CLIMATE_ENTITY as WIDGET_AND_PROTOCOL_TO_CLIMATE_ENTITY, WIDGET_TO_CLIMATE_ENTITY as WIDGET_TO_CLIMATE_ENTITY
from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
