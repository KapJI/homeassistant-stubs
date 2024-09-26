from .. import HomeAssistantOverkizData as HomeAssistantOverkizData
from ..const import DOMAIN as DOMAIN
from .awning import Awning as Awning
from .generic_cover import OverkizGenericCover as OverkizGenericCover
from .vertical_cover import LowSpeedCover as LowSpeedCover, VerticalCover as VerticalCover
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
